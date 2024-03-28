7.1. После создания диаграммы классов в 6 пункте, в 7 пункте база данных "Human Friends" должна быть структурирована в соответствии с этой диаграммой. Например, можно создать таблицы, которые будут соответствовать классам "Pets" и "Pack animals", и в этих таблицах будут поля, которые характеризуют каждый тип животных (например, имена, даты рождения, выполняемые команды и т.д.). 
Начала работы с MySQL и ubuntu после установки:
```bash
sudo service mysql start

```
ввести пароль.
```bash
sudo service mysql status
```
вывод:
```bash
● mysql.service - MySQL Community Server

     Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: enabled)

     Active: active (running) since Wed 2024-03-27 14:27:54 EET; 2h 50min ago

   Main PID: 4946 (mysqld)

     Status: "Server is operational"

      Tasks: 37 (limit: 10975)

     Memory: 365.5M

        CPU: 42.940s

     CGroup: /system.slice/mysql.service

             └─4946 /usr/sbin/mysqld



мар 27 14:27:53 Ra systemd[1]: Starting MySQL Community Server...

мар 27 14:27:54 Ra systemd[1]: Started MySQL Community Server.


```
```bash
yana@Ra:~$ sudo su

root@Ra:/home/yana# mysql -u root -p


```
Вывод:
```bash
Welcome to the MySQL monitor.  Commands end with ; or \g.

Your MySQL connection id is 9

Server version: 8.0.36-0ubuntu0.22.04.1 (Ubuntu)



Copyright (c) 2000, 2024, Oracle and/or its affiliates.



Oracle is a registered trademark of Oracle Corporation and/or its

affiliates. Other names may be trademarks of their respective

owners.



Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
```
Создаём базу данных Human_Friends:
```bash
CREATE DATABASE Human_Friends;

```
Показать базу данных:
```bash
SHOW DATABASES;
```
Вывод:
```bash
+--------------------+

| Database           |

+--------------------+

| Human_Friends      |

| information_schema |

| mysql              |

| performance_schema |

| sys                |

+--------------------+

5 rows in set (0,01 sec)
```
Применить базу данных Human_Friends:
```bash
USE Human_Friends;
```
Создаём таблицы class, type, animal, nursery, owner и заполняем согласно схеме:

```bash
mysql> CREATE TABLE class(class_id INT PRIMARY KEY AUTO_INCREMENT, name_class VARCHAR(25));
mysql> DESCRIBE class;
mysql> INSERT INTO class VALUE (1, 'pets');
mysql> INSERT INTO class VALUE (2, 'pack animals');

```
Наполнение таблицы class:
```bash
mysql> SELECT * FROM class;

+----------+--------------+

| class_id | name_class   |

+----------+--------------+

|        1 | pets         |

|        2 | pack animals |

+----------+--------------+


```
Создание и наполнение таблицы type:
```bash
mysql> CREATE TABLE type(type_id INT PRIMARY KEY AUTO_INCREMENT, name_type VARCHAR(25));
mysql> INSERT INTO type VALUE (1, 'cat');

mysql> INSERT INTO type VALUE (2, 'dog');

mysql> INSERT INTO type VALUE (3, 'hamster');

mysql> INSERT INTO type VALUE (4, 'horse');

mysql> INSERT INTO type VALUE (5, 'camel');

mysql> INSERT INTO type VALUE (6, 'donkey');

```
Наполнение таблицы type:
```bash
mysql> SELECT * FROM type;

+---------+-----------+

| type_id | name_type |

+---------+-----------+

|       1 | cat       |

|       2 | dog       |

|       3 | hamster   |

|       4 | horse     |

|       5 | camel     |

|       6 | donkey    |

+---------+-----------+


```
Создание и наполнение таблицы animal:
```bash
mysql> CREATE TABLE animal (animal_id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(25), type_id INT, class_id INT,  FOREIGN KEY (type_id)  REFERENCES type (type_id) ON DELETE CASCADE, FOREIGN KEY (class_id)  REFERENCES class (class_id) ON DELETE CASCADE, birthday DATE, command VARCHAR(25));
INSERT INTO animal VALUE (1, 'Fido', 2, 1, '2020-01-01', 'Sit, Stay, Fetch');
INSERT INTO animal VALUE (2, 'Whiskers', 1, 1, '2019-05-15', 'Sit, Pounce');

INSERT INTO animal VALUE (3, 'Hammy', 3, 1, '2021-03-10', 'Roll, Hide');

INSERT INTO animal VALUE (4, 'Buddy', 2, 1, '2018-12-10', 'Sit, Paw, Bark');

INSERT INTO animal VALUE (5, 'Smudge', 1, 1, '2020-02-20', 'Sit, Pounce, Scratch');

INSERT INTO animal VALUE (6, 'Peanut', 3, 1, '2021-08-01', 'Roll, Spin');

INSERT INTO animal VALUE (6, 'Peanut', 3, 1, '2021-08-01', 'Roll, Spin');

INSERT INTO animal VALUE (7, 'Bella', 2, 1, '2019-11-11', 'Sit, Stay, Roll');

INSERT INTO animal VALUE (8, 'Oliver', 1, 1, '2020-06-30', 'Meow, Scratch, Jump');

INSERT INTO animal VALUE (9, 'Thunder', 4, 2, '2015-07-21', 'Trot, Canter, Gallop');

INSERT INTO animal VALUE (10, 'Sandy', 5, 2, '2016-11-03', 'Walk, Carry Load');

INSERT INTO animal VALUE (11, 'Eeyore', 6, 2, '2017-09-18', 'Walk, Carry Load, Bray');

INSERT INTO animal VALUE (12, 'Storm', 4, 2, '2014-05-05', 'Trot, Canter');

INSERT INTO animal VALUE (13, 'Dune', 5, 2, '2018-12-12', 'Walk, Sit');

INSERT INTO animal VALUE (14, 'Burro', 6, 2, '2019-01-23', 'Walk, Bray, Kick');

INSERT INTO animal VALUE (15, 'Blaze', 4, 2, '2016-02-29', 'Trot, Jump, Gallop');

INSERT INTO animal VALUE (16, 'Sahara', 5, 2, '2015-08-14', 'Walk, Run');

```
Наполнение таблицы animal:
```bash
mysql> SELECT * FROM animal;

+-----------+----------+---------+----------+------------+------------------------+

| animal_id | name     | type_id | class_id | birthday   | command                |

+-----------+----------+---------+----------+------------+------------------------+

|         1 | Fido     |       2 |        1 | 2020-01-01 | Sit, Stay, Fetch       |

|         2 | Whiskers |       1 |        1 | 2019-05-15 | Sit, Pounce            |

|         3 | Hammy    |       3 |        1 | 2021-03-10 | Roll, Hide             |

|         4 | Buddy    |       2 |        1 | 2018-12-10 | Sit, Paw, Bark         |

|         5 | Smudge   |       1 |        1 | 2020-02-20 | Sit, Pounce, Scratch   |

|         6 | Peanut   |       3 |        1 | 2021-08-01 | Roll, Spin             |

|         7 | Bella    |       2 |        1 | 2019-11-11 | Sit, Stay, Roll        |

|         8 | Oliver   |       1 |        1 | 2020-06-30 | Meow, Scratch, Jump    |

|         9 | Thunder  |       4 |        2 | 2015-07-21 | Trot, Canter, Gallop   |

|        10 | Sandy    |       5 |        2 | 2016-11-03 | Walk, Carry Load       |

|        11 | Eeyore   |       6 |        2 | 2017-09-18 | Walk, Carry Load, Bray |

|        12 | Storm    |       4 |        2 | 2014-05-05 | Trot, Canter           |

|        13 | Dune     |       5 |        2 | 2018-12-12 | Walk, Sit              |

|        14 | Burro    |       6 |        2 | 2019-01-23 | Walk, Bray, Kick       |

|        15 | Blaze    |       4 |        2 | 2016-02-29 | Trot, Jump, Gallop     |

|        16 | Sahara   |       5 |        2 | 2015-08-14 | Walk, Run              |

+-----------+----------+---------+----------+------------+------------------------+

16 rows in set (0,00 sec)


```
Создание и наполнение таблицы owner:
```bash
CREATE TABLE owner (owner_id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(25), phone VARCHAR(25));
INSERT INTO owner VALUE (1, 'Ivanov Ivan', '+78324425613');
INSERT INTO owner VALUE (2, 'Petrov Petr', '+78473211520');
INSERT INTO owner VALUE (3, 'Sidorov Sidor', '+78743281954');
INSERT INTO owner VALUE (4, 'Danilov Danila', '+78542973453');
```
Содержание таблицы owner:
```bash
mysql> SELECT * FROM owner;

+----------+----------------+--------------+

| owner_id | name           | phone        |

+----------+----------------+--------------+

|        1 | Ivanov Ivan    | +78324425613 |

|        2 | Petrov Petr    | +78473211520 |

|        3 | Sidorov Sidor  | +78743281954 |

|        4 | Danilov Danila | +78542973453 |

+----------+----------------+--------------+

4 rows in set (0,00 sec)


```
Создание и наполнение таблицы nursery:
```bash
CREATE TABLE nursery (nursery_id INT PRIMARY KEY AUTO_INCREMENT, animal_id INT, date_in DATE, date_out DATE, owner_id INT);
INSERT INTO nursery VALUE (1, 5, '2020-02-28', NULL, NULL);

INSERT INTO nursery VALUE (2, 7, '2019-11-29', '2019-12-09', 1);
INSERT INTO nursery VALUE (3, 6, '2019-08-25', NULL, NULL);
INSERT INTO nursery VALUE (4, 9, '2015-07-28', NULL, NULL);
INSERT INTO nursery VALUE (5, 6, '2021-08-09', '2021-09-01', 4);
```
Содержание таблицы nursery:
```bash

```