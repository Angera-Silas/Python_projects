-- Active: 1682613043212@@127.0.0.1@3306@web
SELECT * FROM registration;
SELECT * FROM `membersInfo`;
 SELECT * FROM PersonalAccounts;
CREATE TABLE monthlyContribution(Username VARCHAR(50) NOT NULL PRIMARY KEY,Id_no INT(10) NOT NULL UNIQUE, FOREIGN KEY(Username) REFERENCES registration(Username) ON DELETE CASCADE ON UPDATE CASCADE);
ALTER TABLE monthlyContribution ADD FOREIGN KEY (Id_no) REFERENCES membersInfo(Id_no) ON DELETE CASCADE ON UPDATE CASCADE;
INSERT INTO `monthlyContribution` VALUES('sangera',40689254);
SELECT * FROM `monthlyContribution`;
CREATE TABLE PersonalAccounts (Username VARCHAR(50) NOT NULL PRIMARY KEY ,Fixed_Deposit DECIMAL(18,2) DEFAULT 0.00,Personal_Contributions DECIMAL(18,2) DEFAULT 0.00, FOREIGN KEY(Username) REFERENCES monthlyContribution(Username) ON UPDATE CASCADE ON DELETE CASCADE);
INSERT INTO PersonalAccounts(Username) VALUES('sangera');
ALTER TABLE `PersonalAccounts` ADD Savings DECIMAL() AS (Fixed_Deposit+Persnal_Contributions)
