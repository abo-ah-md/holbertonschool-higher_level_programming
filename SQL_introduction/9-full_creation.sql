-- this to create a full table in  the db in the server
CREATE TABLE IF NOT EXISTS second_table(
id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(256) DEFAULT NULL,
score INT NOT NULL,
PRIMARY KEY (id)
);
INSERT INTO second_table (id,name,score) 
values
(1,'John',10),
(2,'Alex',3),
(3,'Bob',14),
(4,'George',8);

