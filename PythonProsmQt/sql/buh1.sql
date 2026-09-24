-- Table: public.buh

-- DROP TABLE IF EXISTS public.buh;

CREATE TABLE IF NOT EXISTS public.buh
(
    data date,
    eda integer,
    benzin integer,
    car integer,
    dosug integer,
    kv_plata integer,
    hos integer,
    dacha integer,
    cat integer,
    dress integer,
    med integer,
    olia integer,
    boria integer,
    proezd integer,
    bania integer,
    gifts integer,
    eltab integer,
    more integer,
    comm character varying COLLATE pg_catalog."default",
    nom integer NOT NULL,
    cosm integer,
    remont integer,
    CONSTRAINT buh_pkey PRIMARY KEY (nom)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.buh
    OWNER to postgres;