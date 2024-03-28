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