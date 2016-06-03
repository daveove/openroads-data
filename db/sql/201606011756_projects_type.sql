ALTER TABLE ONLY projects
    -- `id` should be NOT NULL, but can't insert a NOT NULL column without giving it a value
    ADD COLUMN id character varying(255),
    ADD COLUMN type character varying(255),
    ALTER COLUMN Project_Code DROP NOT NULL,
    ALTER COLUMN Project_Scope DROP NOT NULL
;