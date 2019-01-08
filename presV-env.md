# pressureVessel in Google Cloud
## dependencies
### Acessing cloud instance
- steps
1.![give_path](./docImgs/1.png  "gcloud")
2.![give_path](./docImgs/2.png  "gcloud")
3.![give_path](./docImgs/3.png  "gcloud")
4.![give_path](./docImgs/4.png  "gcloud")

### Uploading files
- file
```bash
gcloud compute scp  E:/index.js  prokura@development-server-ubuntu-16:/home/prokura/
```
 - folder
```bash
gcloud compute scp --recurse  E:/test  prokura@development-server-ubuntu-16:/home/prokura/
```


### Downloading files
- file
```bash
gcloud compute scp   prokura@development-server-ubuntu-16:/home/prokura/test/index.js E:/test
```
- folder
```bash
gcloud compute scp --recurse prokura@development-server-ubuntu-16:/home/prokura/test E:/
```

## Backend Packages
- selected django framework for backend

Packgae | Version
------------ | -------------
python | 3.6.4
Django        |            2.1.1
django-cors-headers      | 2.4.0
djangorestframework    |   3.8.2
conda | 4.4.10

## Frontend Packages
Packgae | Version
------------ | -------------
react | 3.6.4

## Database Essentials
- install postgres-10
### Exporting local db
- export to a file in local
```bash
pg_dump -U nic vesseldb > dbexport.pgsql
```
- upload file to gcloud
```
gcloud compute scp  dbexport.pgsql prokura@development-server-ubuntu-16:/home/prokura/db_import
```
- enter password on prompt
```prokura```


## Creating db
- install postgres
```bash
sudo apt-get install postgresql postgresql-contrib
```
- switch over to postgres account
```bash
sudo -i -u postgres
```
- exit out
```bash
exit
```
- create new role
```bash
sudo -i -u postgres
createuser --interactive
```
- type the username as ```calcgen```
- create the db with dbname same as rolename
```bash
sudo -i -u postgres
createdb calcgen
```
- add the user as linux user
```bash
sudo add user calcgen
```
- create db for project
```bash
sudo -i -u calcgen
psql
createdb vesseldb
\q
```
- log into new db as ```calcgen```
```bash
psql -d vesseldb
```
- set the password for ```calcgen```
```bash
alter user username with encrypted password 'password';
```

- make migration 
```bash
python manage.py migrate
```
- export only table data from specific table
```bash
pg_dump --data-only -U username --table=tablename sourcedb > data.sql
```

- import table in database
```bash
psql -U username databasename < data.sql
```