-- Active: 1682613043212@@127.0.0.1@3306@web
INSERT INTO registration (Username,First_name,Surname,Email_address,Date_of_birth,County_Of_residence) VALUES('hilla012','Hillary','Mumbua','mumbuahillary@gmail.com','2001.11.25','Kitui');
SELECT * FROM registration;
CREATE TABLE membersInfo(Username VARCHAR(50) NOT NULL,Id_no INT(10) NOT NULL PRIMARY KEY,Phone_number INT(12) NOT NULL UNIQUE,Registration_fee DECIMAL(18,2) DEFAULT 0.00,FOREIGN KEY REFERENCES registration(Username) ON DELETE CASCADE ON UPDATE CASCADE,;