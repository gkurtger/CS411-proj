CREATE DATABASE IF NOT EXISTS safeword;
USE safeword;

CREATE TABLE Account (
    email int4  AUTO_INCREMENT,
    service varchar(255),
    password varchar(255),
    PRIMARY KEY (email, service)
);
