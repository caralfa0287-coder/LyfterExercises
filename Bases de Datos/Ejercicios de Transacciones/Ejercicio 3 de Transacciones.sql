ALTER TABLE bills
    DROP CONSTRAINT IF EXISTS status;

ALTER TABLE bills
    ADD CONSTRAINT status
    CHECK (status IN ('pending', 'paid', 'cancelled', 'returned'));


-- Transaccion para retornar los productos.
DO $$
DECLARE
    v_bill_id BIGINT := 1; 
    v_status VARCHAR(20);
    v_item RECORD;
    v_detail_count INTEGER;

BEGIN

-- PASO 1: Verificar que la factura existe.
-- FOR UPDATE bloquea la factura durante la transaccion.
    SELECT status
    INTO v_status
    FROM Bills
    WHERE bill_id = v_bill_id
    FOR UPDATE;

    IF NOT FOUND THEN
        RAISE EXCEPTION
            'Bill ID % does not exist.', v_bill_id;
    END IF;

-- Evitar retornar una factura más de una vez.
    IF v_status = 'returned' THEN
        RAISE EXCEPTION
            'Bill % has already been returned.', v_bill_id;
    END IF;

-- Verificar que la factura tenga productos.
    SELECT COUNT(*)
    INTO v_detail_count
    FROM bill_details
    WHERE bill_id = v_bill_id;

    IF v_detail_count = 0 THEN
        RAISE EXCEPTION
            'Bill % does not contain any products.', v_bill_id;
    END IF;


-- PASO 2: Aumentar el stock de cada producto.
    FOR v_item IN
        SELECT product_id, quantity
        FROM bill_details
        WHERE bill_id = v_bill_id
        ORDER BY product_id
    LOOP

        UPDATE products
        SET stock = stock + v_item.quantity
        WHERE product_id = v_item.product_id;

        IF NOT FOUND THEN
            RAISE EXCEPTION
                'The product with ID % does not exist.',
                v_item.product_id;
        END IF;

    END LOOP;


-- PASO 3: Marcar la factura como retornada.
    UPDATE bills
    SET status = 'returned'
    WHERE bill_id = v_bill_id;


    RAISE NOTICE
        'Bill % was returned successfully.',
        v_bill_id;

END;
$$ LANGUAGE plpgsql;