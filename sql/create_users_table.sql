/* зарегистрированные пользователи сервиса */
CREATE TABLE users (
  uid INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  firstname VARCHAR(100) NULL,
  lastname VARCHAR(100) NULL,
  email VARCHAR(120) NOT NULL UNIQUE,
  pwdhash VARCHAR(100) NOT NULL,
  prefered_lang VARCHAR(45) NULL,
  created_date DATETIME NULL
);

