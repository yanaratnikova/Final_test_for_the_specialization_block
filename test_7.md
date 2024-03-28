- Удалить записи о верблюдах :
```bash
DELETE FROM animal WHERE type_id = 5;
```
Рузультат:
```bash
mysql> SELECT name, name_type AS type, command FROM animal INNER JOIN type ON animal.type_id = type.type_id;

+----------+---------+------------------------+

| name     | type    | command                |

+----------+---------+------------------------+

| Whiskers | cat     | Sit, Pounce            |

| Smudge   | cat     | Sit, Pounce, Scratch   |

| Oliver   | cat     | Meow, Scratch, Jump    |

| Fido     | dog     | Sit, Stay, Fetch       |

| Buddy    | dog     | Sit, Paw, Bark         |

| Bella    | dog     | Sit, Stay, Roll        |

| Hammy    | hamster | Roll, Hide             |

| Peanut   | hamster | Roll, Spin             |

| Thunder  | horse   | Trot, Canter, Gallop   |

| Storm    | horse   | Trot, Canter           |

| Blaze    | horse   | Trot, Jump, Gallop     |

| Eeyore   | donkey  | Walk, Carry Load, Bray |

| Burro    | donkey  | Walk, Bray, Kick       |

+----------+---------+------------------------+

13 rows in set (0,00 sec)


```
объединить таблицы лошадей и ослов:
```bash
CREATE TEMPORARY TABLE Horses_and_donkeys AS SELECT * FROM animal WHERE type_id = 4 || type_id = 6;


```
Результат:
```bash
mysql> SELECT * FROM Horses_and_donkeys INNER JOIN type ON Horses_and_donkeys.type_id = type.type_id;

+-----------+---------+---------+----------+------------+------------------------+---------+-----------+

| animal_id | name    | type_id | class_id | birthday   | command                | type_id | name_type |

+-----------+---------+---------+----------+------------+------------------------+---------+-----------+

|         9 | Thunder |       4 |        2 | 2015-07-21 | Trot, Canter, Gallop   |       4 | horse     |

|        12 | Storm   |       4 |        2 | 2014-05-05 | Trot, Canter           |       4 | horse     |

|        15 | Blaze   |       4 |        2 | 2016-02-29 | Trot, Jump, Gallop     |       4 | horse     |

|        11 | Eeyore  |       6 |        2 | 2017-09-18 | Walk, Carry Load, Bray |       6 | donkey    |

|        14 | Burro   |       6 |        2 | 2019-01-23 | Walk, Bray, Kick       |       6 | donkey    |

+-----------+---------+---------+----------+------------+------------------------+---------+-----------+

5 rows in set (0,00 sec)


```
   - Создать новую таблицу для животных в возрасте от 1 до 3 лет и вычислить их возраст с точностью до месяца.
   ```bash
   CREATE TEMPORARY TABLE 1_3_age AS SELECT animal_id, name, type_id, class_id, birthday, command, TIMESTAMPDIFF(MONTH, birthday, NOW()) AS age FROM animal WHERE TIMESTAMPDIFF(MONTH, birthday, NOW()) BETWEEN 12 AND 36;
   ```
   Результат:
   ```bash
   mysql> SELECT * FROM 1_3_age;

+-----------+--------+---------+----------+------------+------------+------+

| animal_id | name   | type_id | class_id | birthday   | command    | age  |

+-----------+--------+---------+----------+------------+------------+------+

|         3 | Hammy  |       3 |        1 | 2021-03-10 | Roll, Hide |   36 |

|         6 | Peanut |       3 |        1 | 2021-08-01 | Roll, Spin |   31 |

+-----------+--------+---------+----------+------------+------------+------+

2 rows in set (0,00 sec)


   ```
Объединить две таблицы в одну, сохраняя информацию о принадлежности к исходным таблицам:
   ```bash
   mysql> SELECT animal_id, name, 'animal' AS source_table

    -> FROM animal

    -> UNION ALL

    -> SELECT class_id, name_class, 'class' AS source_table

    -> FROM class;


   ```
   Вывод:
   ```bash
   +-----------+--------------+--------------+

| animal_id | name         | source_table |

+-----------+--------------+--------------+

|         1 | Fido         | animal       |

|         2 | Whiskers     | animal       |

|         3 | Hammy        | animal       |

|         4 | Buddy        | animal       |

|         5 | Smudge       | animal       |

|         6 | Peanut       | animal       |

|         7 | Bella        | animal       |

|         8 | Oliver       | animal       |

|         9 | Thunder      | animal       |

|        11 | Eeyore       | animal       |

|        12 | Storm        | animal       |

|        14 | Burro        | animal       |

|        15 | Blaze        | animal       |

|         1 | pets         | class        |

|         2 | pack animals | class        |

+-----------+--------------+--------------+

15 rows in set (0,00 sec)


   ```
   