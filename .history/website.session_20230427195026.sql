-- Active: 1682613043212@@127.0.0.1@3306@web
CREATE TABLE registration (Username VARCHAR(50) NOT NULL PRIMARY KEY,First_name CHAR(20) NOT NULL,Surname CHAR(20) NOT NULL,Email_address VARCHAR(100) NOT NULL UNIQUE,Date_of_birth DATE,Nationality CHAR(20) DEFAULT "Kenyan", County_Of_residence CHAR(20) DEFAULT "Nairobi");
IN