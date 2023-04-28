-- Active: 1682613043212@@127.0.0.1@3306@web
CREATE TABLE registration (Username VARCHAR(50) NOT NULL PRIMARY KEY,First_name CHAR(20) NOT NULL,Surname CHAR(20) NOT NULL,Email_address VARCHAR(100) NOT NULL UNIQUE,Date_o
INSERT INTO registration (Username,First_name,Surname,Email_address,Date_of_birth,County_Of_residence) VALUES('sangera','Silas','Angera','angerasilas@gmail.com','2001.11.30','Trans-Nzoia')
SELECT * FROM registration;