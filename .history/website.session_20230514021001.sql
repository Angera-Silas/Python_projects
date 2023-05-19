-- Active: 1682613043212@@127.0.0.1@3306@web
SELECT * FROM registration;
SELECT * FROM `membersInfo`;
 SELECT * FROM PersonalAccounts;
CREATE TABLE monthlyContribution(Username VARCHAR(50) NOT NULL PRIMARY KEY,id_no INT(10) NOT NULL, FOREIGN KEY(Username) REFERENCES registration(Username));
DROP M