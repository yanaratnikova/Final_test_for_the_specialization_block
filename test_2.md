3. Работа с MySQL в Linux. “Установить MySQL на вашу вычислительную машину ”
- Обновление репозиториев пакетов сервера:
```bash
sudo apt update
```
- Установка пакетов MySQL:
```bash
sudo apt install mysql-server
```
- Проверить версию установленного пакета:
```bash
mysql -V

```
- Результат:
mysql  Ver 8.0.36-0ubuntu0.22.04.1 for Linux on x86_64 ((Ubuntu))
-Подключить дополнительный репозиторий MySQL и установить один из пакетов из этого репозитория:
```bash
    sudo add-apt-repository 'deb http://repo.mysql.com/apt/ubuntu/ focal mysql-5.7'

    sudo apt update

    sudo apt install mysql-server-5.7
```
