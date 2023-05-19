-- Active: 1682613043212@@127.0.0.1@3306@web
INSERT INTO registration (Username,First_name,Surname,Email_address,Date_of_birth,County_Of_residence) VALUES('hilla012','Hillary','Mumbua','mumbuahillary@gmail.com','2001.11.25','Kitui');
SELECT * FROM registration;
SELECT * FROM `membersInfo`;
CREATE TABLE PersonalAccounts(Fixed_Deposit DECIMAL(18,2) DEFAULT 0.00,Personal_contributions DECIMAL(18,2) DEFAULT 0.00);
ALTER TABLE `membersInfo` MODIFY Gender CHAR(10) NOT NULL;
ALTER TABLE `membersInfo` MODIFY Physical_challenged BOOLEAN ;
SELECT * FROM `membersInfo`;
ALTER TABLE registration MODIFY Age INT AS (TIMESTAMPDIFF(YEAR,Date_of_birth,Registration_Date));