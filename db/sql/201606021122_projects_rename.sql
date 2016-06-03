ALTER TABLE ONLY projects RENAME COLUMN Project_Code TO code;
ALTER TABLE ONLY projects RENAME COLUMN Road_Name TO name;
ALTER TABLE ONLY projects RENAME COLUMN Project_Scope TO scope;
-- Should need to be lower-cased, but because of how Postgres casts names this isn't necessary
-- ALTER TABLE ONLY projects RENAME COLUMN "Year" TO year;
ALTER TABLE ONLY projects RENAME COLUMN Length_KM TO length;
ALTER TABLE ONLY projects RENAME COLUMN Project_Cost TO cost;
