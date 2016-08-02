CREATE TABLE user_words (
  id INT NOT NULL AUTO_INCREMENT,
  user_id INT NOT NULL,
  word VARCHAR(255) NOT NULL,
  translation VARCHAR(500) NOT NULL,
  language VARCHAR(50) NOT NULL,
  sound VARCHAR(200) NULL,
  repeats SMALLINT(5) NULL,
  last_repeat DATETIME NULL,
  trained TINYINT(1) NULL,
  created_date DATETIME NULL,
  udate DATETIME NULL,
  list VARCHAR(80) NULL,
  example VARCHAR(500) NULL,
  transcription VARCHAR(100) NULL,
  mob_marked INT(11) NULL,
  mob_flags INT(11) NULL,
  mob_retention_max INT(10) NULL,
  mob_retention INT(10) NULL,
  mob_incorrect INT(10) NULL,
  mob_keyword VARCHAR(100) NULL,
  PRIMARY KEY (id, user_id),
  UNIQUE INDEX id_UNIQUE (id ASC),
  CONSTRAINT user
    FOREIGN KEY (user_id)
    REFERENCES users (uid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);
