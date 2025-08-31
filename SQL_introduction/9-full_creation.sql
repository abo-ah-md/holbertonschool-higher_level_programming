-- this to create a full table in  the db in the server
CREATE TABLE IF NOT EXISTS second_table(
id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(256) DEFAULT NULL,
score INT NOT NULL,
PRIMARY KEY (id)
);
ALTER TABLE second_table AUTO_INCREMENT = 1;
INSERT INTO second_table (name,score) 
values
('John',10),
('Alex',3),
('Bob',14),
('George',8);

