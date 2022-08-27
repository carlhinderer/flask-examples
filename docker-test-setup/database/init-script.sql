CREATE DATABASE myappdb;
CREATE USER myappuser WITH PASSWORD 'myapppw';
GRANT ALL PRIVILEGES ON DATABASE myappdb TO myappuser;

\c myappdb;

CREATE TABLE hobbies(
   hobby_id serial PRIMARY KEY,
   hobby VARCHAR (255) UNIQUE NOT NULL
);

INSERT INTO hobbies(hobby) VALUES('swimming');
INSERT INTO hobbies(hobby) VALUES('diving');
INSERT INTO hobbies(hobby) VALUES('jogging');
INSERT INTO hobbies(hobby) VALUES('dancing');
INSERT INTO hobbies(hobby) VALUES('cooking');