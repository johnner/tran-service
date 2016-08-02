/*Пользователь БД*/
CREATE USER 'web'@'localhost' IDENTIFIED BY '12345';
GRANT SELECT ON tran.* TO 'web'@'localhost';
GRANT INSERT ON tran.* TO 'web'@'localhost';
GRANT UPDATE ON tran.* TO 'web'@'localhost';
GRANT DELETE ON tran.* TO 'web'@'localhost';
GRANT EXECUTE ON tran.* TO 'web'@'localhost';

