# SQL_more_queries

A comprehensive collection of SQL scripts and database exercises covering advanced MySQL usage, constraints, privileges, and relational data modeling. Designed for the Holberton School curriculum, targeting mastery of querying techniques, multi-table relations, user permissions, and real database problem-solving.

---

## 📖 Table of Contents

- [Project Description](#project-description)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Resources](#resources)
- [Scripts & Tasks](#scripts--tasks)
- [Files](#files)
- [Extra Database Design Resources](#extra-database-design-resources)

---

## Project Description

This directory contains mandatory tasks focused on MySQL 8.0. Each SQL script addresses specific operations including privilege management, user creation, table constraints, multi-table queries (joins and subqueries), and best practices for relational design. All scripts include thorough comments, use uppercase SQL keywords as per the style guide, and are compatible with Ubuntu 20.04 LTS. 

---

## Learning Objectives

By the end of this project, you will be able to:

- **Create MySQL users** and manage their privileges to databases/tables.
- **Understand and use constraints:** `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `UNIQUE`
- **Design and query multi-table relations:** retrieve data using subqueries and joins.
- **Apply advanced SQL techniques:** multiple joins, distinct keyword, join types, unions, subqueries.
- **Manage real database structures:** import dumps, write scripts with error resistance, enforce style guide.
---

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- Platform: Ubuntu 20.04 LTS, MySQL 8.0 (version 8.0.25)
- All SQL files must end with a new line and start with a comment describing the task.
- All SQL keywords must be uppercase (e.g., `SELECT`, `WHERE`).
- Mandatory `README.md` at the root of the project folder.
- Scripts must handle existing entities without errors (`IF NOT EXISTS`).
- SQL queries must have immediate comments above them.
- Length of files may be tested using `wc`.

---

## Resources

- [How To Create a New User and Grant Permissions in MySQL](https://intranet.hbtn.io/rltoken/1tuxYhEv__bmrwkAicbjpA)
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://intranet.hbtn.io/rltoken/km4VxJIBhjKVfiWEBETk-w)
- [MySQL constraints](https://intranet.hbtn.io/rltoken/AHI2a6vFyr8h4LeI6xK96w)
- [Basic query operation: the join](https://intranet.hbtn.io/rltoken/iwZZ9bwumE2xjRjvK-yCxQ)
- [SQL technique: multiple joins and the distinct keyword](https://intranet.hbtn.io/rltoken/Hy6OBC0V9kzCRA5Xl0L7gw)
- [SQL technique: join types](https://intranet.hbtn.io/rltoken/MQFjsE5PICdbya6ef9fglw)
- [SQL technique: subqueries](https://intranet.hbtn.io/rltoken/L7aZyitKEI69svRrvEt9Ag)
- [SQL technique: union and minus](https://intranet.hbtn.io/rltoken/jidXwpyYDU7yhJspxvx0kw)
- [MySQL Cheat Sheet](https://intranet.hbtn.io/rltoken/g8QlxhHt2_WHdIXE-2oYYw)
- [The Seven Types of SQL Joins](https://intranet.hbtn.io/rltoken/o6faV44f8S34zW3FiO5Mgg)
- [MySQL Tutorial](https://intranet.hbtn.io/rltoken/T3VjE1yBfwJcd1hDD4tItw)
- [SQL Style Guide](https://intranet.hbtn.io/rltoken/0NaQZjOUvQuWy0xGPhTkVw)
- [MySQL 8.0 SQL Statement Syntax](https://intranet.hbtn.io/rltoken/R5KAnzO4iwYo2LgD3eKL8A)

**Extra (design focus):**
- [Design](https://intranet.hbtn.io/rltoken/A81_Vk2TV-f_f5wG0HK6Zw)
- [Normalization](https://intranet.hbtn.io/rltoken/cwgE_DVy7l3ap6lCVJsPZQ)
- [ER Modeling](https://intranet.hbtn.io/rltoken/1JFNpSloiEAI7aLW2rnyKw)

---

## Scripts & Tasks

Each numbered SQL script in this directory covers a dedicated exercise:

- `0-privileges.sql` : List all privileges for specific MySQL users.
- `1-create_user.sql` : Create a privileged user.
- `2-create_read_user.sql` : Create a read-only user and database.
- `3-force_name.sql` : Table with a `NOT NULL` constraint.
- `4-never_empty.sql` : Table with a default `id` value.
- `5-unique_id.sql` : Table requiring a unique `id`.
- `6-states.sql` : Database/table creation with unique, auto-increment PRIMARY KEY.
- `7-cities.sql` : Table with a FOREIGN KEY referencing another table.
- `8-cities_of_california_subquery.sql` : List cities by state using subquery (no JOIN).
- `9-cities_by_state_join.sql` : Join two tables to list cities and states.
- `10-genre_id_by_show.sql` : List shows with at least one linked genre.
- `11-genre_id_all_shows.sql` : List all shows, with genre_id or NULL.
- `12-no_genre.sql` : List shows with no genres.
- `13-count_shows_by_genre.sql` : List all genres and count of linked shows (descending order).
- `14-my_genres.sql` : List all genres for a specific show ("Dexter").
- `15-comedy_only.sql` : List shows linked to the "Comedy" genre.
- `16-shows_by_genre.sql` : List all shows and their linked genres, NULL if none.

All scripts suitable for automated execution:  
`cat script.sql | mysql -hlocalhost -uroot -p [database-name]`

---

## Files

This folder contains:

- `README.md` : This documentation
- SQL scripts (numbered as above)
- `dump.sql` : Example usage for importing SQL dump files

---

## Extra Database Design Resources

- Entity-Relationship modeling and normalization rationales
- Real-world design guidelines to avoid redundancy and maintain relational integrity

---

## Usage

1. **Setup MySQL 8.0**:  
   For Ubuntu 20.04 LTS, install using:
```
sudo apt update
sudo apt install mysql-server
```

2. **Connect to MySQL**:  
```
sudo mysql
```

3. **Import SQL dump** (example):  
```
curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
```

4. **Execute scripts**:  
```
cat script.sql | mysql -hlocalhost -uroot -p [database-name]
```

---

## Credits

Project authored for [Holberton School](https://www.holbertonschool.com/)  
All exercises conform to Holberton's permanent style, error handling, and documentation conventions.

---
