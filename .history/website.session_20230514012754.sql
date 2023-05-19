-- Active: 1682613043212@@127.0.0.1@3306@web
INSERT INTO registration (Username,First_name,Surname,Email_address,Date_of_birth,County_Of_residence) VALUES('hilla012','Hillary','Mumbua','mumbuahillary@gmail.com','2001.11.25','Kitui');
SELECT * FROM registration;
CREATE TABLE membersInfo(Username VARCHAALUES('sR(50) NOT NULL,Id_no INT(10) NOT NULL PRIMARY KEY,Phone_number INT(12) NOT NULL UNIQUE,Registration_fee DECIMAL(18,2) DEFAULT 0.00,FOREIGN KEY(Username) REFERENCES registration(Username) ON DELETE CASCADE ON UPDATE CASCADE);
INSERT INTO membersInfo Vangera',40689254,797630228,1000);
ALTER TABLE membersInfo MODIFY Password VARCHAR(10) NOT NULL UNIQUE;
UPDATE `membersInfo` SET `Phone_number` = '+254797630228' WHERE Username = 'sangera';
SELECT * FROM `membersInfo`;
INSERT INTO `membersInfo` VALUES('mainageoff',39342023,'+25471169320092',1000);
CREATE TABLE PersonalAccounts(Fixed_Deposit DECIMAL(18,2) DEFAULT 0.00,Personal_contributions DECIMAL(18,2) DEFAULT 0.00);
ALTER TABLE `membersInfo` MODIFY Gender CHAR(10) NOT NULL;
ALTER TABLE `membersInfo` MODIFY Physical_challenged BOOLEAN ;
SELECT * FROM `membersInfo`;
ALTER TABLE registration MODIFY Age INT AS (TIMESTAMPDIFF(YEAR,Date_of_birth,Registration_Date)) CHECK (IF );