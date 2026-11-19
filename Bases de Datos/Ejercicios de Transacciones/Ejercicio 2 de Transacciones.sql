DO $$
DECLARE
    -- ID del usuario que realiza la compra
    v_user_id BIGINT := 1;

    -- Productos y cantidades que desea comprar
    v_items JSONB := '[
        {"product_id": 1, "quantity": 2},
        {"product_id": 2, "quantity": 1}
    ]'::jsonb;

    v_item RECORD;
    v_stock INTEGER;
    v_price NUMERIC(10,2);
    v_total NUMERIC(12,2) := 0;
    v_bill_id BIGINT;
    v_item_count INTEGER;
    v_distinct_product_count INTEGER;

BEGIN

    -- 1. Verificar que existan productos en la compra
    IF jsonb_typeof(v_items) IS DISTINCT FROM 'array' THEN
        RAISE EXCEPTION 'The shopping list is not valid.';
    END IF;

    IF jsonb_array_length(v_items) = 0 THEN
        RAISE EXCEPTION 'The purchase must contain products.';
    END IF;

    -- 2. Evitar productos repetidos
    SELECT COUNT(*), COUNT(DISTINCT item.product_id)
    INTO v_item_count, v_distinct_product_count
    FROM jsonb_to_recordset(v_items)
        AS item(product_id BIGINT, quantity INTEGER);

    IF v_item_count <> v_distinct_product_count THEN
        RAISE EXCEPTION 'There are duplicate items in the purchase.';
    END IF;

    -- 3. Verificar que el usuario exista
    PERFORM 1
    FROM Users
    WHERE user_id = v_user_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'The user with ID % does not exist.', v_user_id;
    END IF;

    -- 4. Verificar existencia y stock de cada producto
    FOR v_item IN
        SELECT item.product_id, item.quantity
        FROM jsonb_to_recordset(v_items)
            AS item(product_id BIGINT, quantity INTEGER)
        ORDER BY item.product_id
    LOOP

        IF v_item.product_id IS NULL
           OR v_item.quantity IS NULL
           OR v_item.quantity <= 0 THEN
            RAISE EXCEPTION
                'The product must have a valid ID and quantity.';
        END IF;

        -- Bloquear la fila mientras se procesa la compra
        SELECT price, stock
        INTO v_price, v_stock
        FROM Products
        WHERE product_id = v_item.product_id
        FOR UPDATE;

        IF NOT FOUND THEN
            RAISE EXCEPTION
                'The product with ID % does not exist.',
                v_item.product_id;
        END IF;

        IF v_stock < v_item.quantity THEN
            RAISE EXCEPTION
                'Insufficient stock for product %. Available: %, requested: %.',
                v_item.product_id, v_stock, v_item.quantity;
        END IF;

        -- Calcular el total
        v_total := v_total + (v_price * v_item.quantity);

    END LOOP;

    -- 5. Insertar la factura
    INSERT INTO Bills (user_id, date, status, total)
    VALUES (v_user_id, CURRENT_TIMESTAMP, 'pending', v_total)
    RETURNING bill_id INTO v_bill_id;

    -- 6. Insertar los detalles y descontar el inventario
    FOR v_item IN
        SELECT item.product_id, item.quantity
        FROM jsonb_to_recordset(v_items)
            AS item(product_id BIGINT, quantity INTEGER)
        ORDER BY item.product_id
    LOOP

        SELECT price
        INTO v_price
        FROM Products
        WHERE product_id = v_item.product_id;

        INSERT INTO Bill_Details
            (bill_id, product_id, quantity, unit_price)
        VALUES
            (v_bill_id, v_item.product_id, v_item.quantity, v_price);

        UPDATE Products
        SET stock = stock - v_item.quantity
        WHERE product_id = v_item.product_id;

    END LOOP;

    RAISE NOTICE
        'Purchase made. Invoice: %, Total: %',
        v_bill_id, v_total;

END;
$$ LANGUAGE plpgsql;