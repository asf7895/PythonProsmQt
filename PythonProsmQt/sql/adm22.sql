-- Table: public.admin1

-- DROP TABLE IF EXISTS public..admin1;


CREATE TABLE IF NOT EXISTS public.admin1
(
  login character varying COLLATE pg_catalog."default",
  pwd character varying COLLATE pg_catalog."default",
  email character varying COLLATE pg_catalog."default",
  year character varying COLLATE pg_catalog."default",
  city character varying COLLATE pg_catalog."default",
  prof character varying COLLATE pg_catalog."default",
  fullname character varying COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.admin1
    OWNER to postgres;