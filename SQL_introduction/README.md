# SQL_introduction

This directory contains a set of introductory tasks for learning SQL using MySQL 8.0, with all code tested on Ubuntu 22.04 LTS.

---

## Resources

Recommended reading and tutorials:
- What is Database & SQL?
- Install MySQL (MySQL Server)
- A Basic MySQL Tutorial
- Basic SQL statements: DDL and DML
- Basic queries: SQL and RA
- SQL technique: functions
- SQL technique: subqueries
- What makes the big difference between a backtick and an apostrophe?
- MySQL Cheat Sheet
- MySQL 8.0 SQL Statement Syntax

Due to temporary bugs with some resources above, you can find most of the information [here].

---

## Learning Objectives

By completing this project, you will be able to explain to anyone (without using Google):

- What is a database?
- What is a relational database?
- What does SQL stand for?
- What is MySQL?
- How to create a database in MySQL
- What do DDL and DML mean?
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE or DELETE data
- What are subqueries?
- How to use MySQL functions

---

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files run on Ubuntu 22.04 LTS with MySQL 8.0 (version 8.0.25)
- Each file ends with a new line
- Each SQL query is preceded by a comment describing the task
- Each file starts with a comment describing the task
- All SQL keywords are in **UPPERCASE** (e.g. SELECT, WHERE)
- A README.md at the root of the folder is mandatory
- The length of your files will be tested using `wc`

---

## Usage

The sandbox is available to run MySQL commands.

### Example for running SQL script:
```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$ cat my_script.sql | mysql -hlocalhost -uroot -p
```

---

### MySQL Installation

- Update package list:

```
- Install MySQL Server:

```
- Install MySQL Server:

```
apt install -y mysql-server
```
- Confirm installation:
```
mysql --version
```
- Start MySQL:
  ```
  service mysql start
  ```
  - Access MySQL CLI:
```
mysql -uroot
```

### For Ubuntu 20.04 (legacy image):

- Credentials: root/root
- Start MySQL before use:

```
service mysql start
```

---

## Task Overview

Each SQL script corresponds to a numbered task in this directory:

| Script                       | Task Description                                    |
|------------------------------|-----------------------------------------------------|
| 0-list_databases.sql         | List all databases in MySQL server                  |
| 1-create_database_if_missing.sql | Create database `hbtn_0c_0` if missing           |
| 2-remove_database.sql        | Delete database `hbtn_0c_0` if exists               |
| 3-list_tables.sql            | List all tables in a database                       |
| 4-first_table.sql            | Create table `first_table` (`id INT`, `name VARCHAR(256)`) |
| 5-full_table.sql             | Print full `CREATE TABLE` statement for `first_table` |
| 6-list_values.sql            | List all rows from `first_table`                    |
| 7-insert_value.sql           | Insert row (`id=89`, `name=Best School`) in `first_table` |
| 8-count_89.sql               | Count rows with `id=89` in `first_table`            |
| 9-full_creation.sql          | Create `second_table` and insert multiple rows      |
| 10-top_score.sql             | List `second_table` records ordered by score (desc) |
| 11-best_score.sql            | List records where score >= 10 (desc)               |
| 12-no_cheating.sql           | Update score of Bob to 10 using only name           |
| 13-change_class.sql          | Delete records with score <= 5                      |
| 14-average.sql               | Compute average score in `second_table`             |
| 15-groups.sql                | List count of records for each score (desc)         |
| 16-no_link.sql               | List records where name is NOT NULL (desc)          |

---

## Example Workflow

1. **List Databases**
 - Run:
   ```
   cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
   ```
2. **Create Database**
 - Run:
   ```
   cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
   ```
3. **Delete Database**
 - Run:
   ```
   cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
   ```
4. **List Tables**
 - Run:
   ```
   cat 3-list_tables.sql | mysql -hlocalhost -uroot -p <YOUR_DATABASE>
   ```

(Continue as above for remaining tasks.)

---

## File Structure

```
SQL_introduction/
├── 0-list_databases.sql
├── 1-create_database_if_missing.sql
├── 2-remove_database.sql
├── 3-list_tables.sql
├── 4-first_table.sql
├── 5-full_table.sql
├── 6-list_values.sql
├── 7-insert_value.sql
├── 8-count_89.sql
├── 9-full_creation.sql
├── 10-top_score.sql
├── 11-best_score.sql
├── 12-no_cheating.sql
├── 13-change_class.sql
├── 14-average.sql
├── 15-groups.sql
├── 16-no_link.sql
└── README.md
```

---

## Style Guide

- Start each SQL file with a comment describing the task
- Precede each SQL query with a comment describing it
- Use uppercase for all SQL keywords
- End each file with a newline

---

## Author

- Repo maintained by [abo-ah-md](https://github.com/abo-ah-md)
