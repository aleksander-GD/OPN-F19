CREATE DATABASE person;

USE person;

CREATE TABLE personTable (
	personID int(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	firstname VARCHAR(100) NOT NULL,
	lastname VARCHAR(100) NOT NULL
);

INSERT INTO
	personTable (firstname, lastname)
VALUES
	("Aleksander", "Duszkiewicz")