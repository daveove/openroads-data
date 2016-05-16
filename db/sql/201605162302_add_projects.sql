--
-- Name: projects; Type: TABLE; Schema: public; Owner: -; Tablespace:
--

CREATE TABLE projects (
Project_Code character varying(255) NOT NULL,
adminids bigint[] NOT NULL,
Project_Scope character varying(255) NOT NULL,
Year integer,
Road_Name character varying(255),
Length_KM real,
Project_Cost real
);
