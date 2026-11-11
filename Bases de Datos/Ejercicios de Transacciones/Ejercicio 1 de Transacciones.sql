--
-- PostgreSQL database dump
--

\restrict IPik1mIdunPwEcxBzFiusDaV4pibUrWDZxOvxw7qonlUmaJqwgYpIIefpKcx85A

-- Dumped from database version 18.6
-- Dumped by pg_dump version 18.6

-- Started on 2026-11-10 18:47:16

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 226 (class 1259 OID 24665)
-- Name: bill_details; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bill_details (
    detail_id integer NOT NULL,
    bill_id integer NOT NULL,
    product_id integer NOT NULL,
    quantity integer NOT NULL,
    unit_price numeric NOT NULL,
    subtotal numeric GENERATED ALWAYS AS (((quantity)::numeric * unit_price)) STORED,
    CONSTRAINT quantity CHECK ((quantity > 0)),
    CONSTRAINT unit_price CHECK ((unit_price >= (0)::numeric))
);


ALTER TABLE public.bill_details OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 24664)
-- Name: bill_details_detail_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.bill_details ALTER COLUMN detail_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.bill_details_detail_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 224 (class 1259 OID 24622)
-- Name: bills; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bills (
    bill_id integer NOT NULL,
    user_id integer,
    date timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    status character varying(20),
    total numeric DEFAULT 0
);


ALTER TABLE public.bills OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 24621)
-- Name: bills_bill_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.bills ALTER COLUMN bill_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.bills_bill_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 222 (class 1259 OID 24594)
-- Name: products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.products (
    product_id integer NOT NULL,
    name character varying(50) NOT NULL,
    description text,
    price numeric NOT NULL,
    stock integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.products OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 24593)
-- Name: products_product_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.products ALTER COLUMN product_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.products_product_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 220 (class 1259 OID 24581)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    name character varying(100) NOT NULL,
    email character varying(150)[] NOT NULL,
    phone text
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 24580)
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.users ALTER COLUMN user_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.users_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 4888 (class 2606 OID 24679)
-- Name: bill_details bill_details_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bill_details
    ADD CONSTRAINT bill_details_pkey PRIMARY KEY (detail_id);


--
-- TOC entry 4886 (class 2606 OID 24631)
-- Name: bills bills_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bills
    ADD CONSTRAINT bills_pkey PRIMARY KEY (bill_id);


--
-- TOC entry 4880 (class 2606 OID 24592)
-- Name: users email; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT email UNIQUE (email);


--
-- TOC entry 4884 (class 2606 OID 24605)
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (product_id);


--
-- TOC entry 4875 (class 2606 OID 24705)
-- Name: bills status; Type: CHECK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE public.bills
    ADD CONSTRAINT status CHECK (((status)::text = ANY ((ARRAY['pending'::character varying, 'paid'::character varying, 'cancelled'::character varying])::text[]))) NOT VALID;


--
-- TOC entry 4876 (class 2606 OID 24706)
-- Name: bills total; Type: CHECK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE public.bills
    ADD CONSTRAINT total CHECK ((total >= (0)::numeric)) NOT VALID;


--
-- TOC entry 4882 (class 2606 OID 24590)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- TOC entry 4890 (class 2606 OID 24680)
-- Name: bill_details bill_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bill_details
    ADD CONSTRAINT bill_id FOREIGN KEY (bill_id) REFERENCES public.bills(bill_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 4891 (class 2606 OID 24685)
-- Name: bill_details product_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bill_details
    ADD CONSTRAINT product_id FOREIGN KEY (product_id) REFERENCES public.products(product_id) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 4889 (class 2606 OID 24700)
-- Name: bills user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bills
    ADD CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES public.users(user_id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;


-- Completed on 2026-11-10 18:47:17

--
-- PostgreSQL database dump complete
--

\unrestrict IPik1mIdunPwEcxBzFiusDaV4pibUrWDZxOvxw7qonlUmaJqwgYpIIefpKcx85A

