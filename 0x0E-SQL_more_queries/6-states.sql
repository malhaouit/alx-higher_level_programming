-- Creates the database `hbtn_0d_usa` and the table `states`.
-- In table states: the `id` is unique, auto generated, can’t be null and is a primary key.
-- In table states: the `name` can't be null.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);
