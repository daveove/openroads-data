--
-- Name: projecttasks; Type: TABLE; Schema: public; Owner: -; Tablespace:
--

CREATE TABLE projecttasks (
	id serial PRIMARY KEY,
	type character varying(255) NOT NULL,
	adminids bigint[] NOT NULL
);
