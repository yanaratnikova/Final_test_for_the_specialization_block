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
История команд:
yana@Ra:~$ history
```
    1  sudo apt install terminator

    2  sudo dpkg --configure -a

    3  sudo apt install terminator

    4  sudo apt install gcc make perl -y

    5  sudo ./VBoxLinuxAdditions.run 

    6  reboot

    7  pwd

    8  sudo mkdir/home/yana/Final_test

    9  mkdir Final_test

   10  cd Final_test

   11  cat > Pets

   12  cat Pets

   13  cat > Pack_animals

   14  cat Pets Pack_animals > file3

   15  cat file3

   16  mv file3 Human_Friends

   17  ls Final_test

   18  pwd

   19  is

   20  ls

   21  mkdir new_folder

   22  mv Human_Friends new_folder

   23  ls

   24  cd ..

   25  pwd

   26  sudo apt update

   27  sudo apt upgrade

   28  sudo apt install mysql-server

   29  systemctl status myaql.service

   30  mysql -V

   31  sudo apt update

   32  history

```
 - Установить и удалить deb-пакет mc:
 ```bash
 sudo apt-get install wget

 wget http://archive.ubuntu.com/ubuntu/pool/universe/m/mc/mc_4.8.24-2ubuntu1_amd64.
 
sudo dpkg -i mc_4.8.27-1_amd64.deb

mc

sudo dpkg -r mc
 ```
- История комманд:
```bash
  39  apt-get install wget

   40  sudo apt-get install wget

   41  wget http://archive.ubuntu.com/ubuntu/pool/universe/m/mc/mc_4.8.24-2ubuntu1_amd64.deb

   42  sudo dpkg -i mc_4.8.27-1_amd64.deb

   43  mc

   44  sudo dpkg -r mc

   45  history


```
