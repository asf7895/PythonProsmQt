-- Table: public.opros1

-- DROP TABLE IF EXISTS public.opros1;


CREATE TABLE IF NOT EXISTS public.opros1
(
  r_answer integer ,
  user character varying COLLATE pg_catalog."default",
  data1 date,
  num_answer integer

)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.opros1
    OWNER to postgres;