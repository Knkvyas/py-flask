<<<<<<< HEAD
# Ku8e it Out

## Run these below commands in the terminal to build and run the project

```
python3 -m venv venv
```
```
source venv/bin/activate
```
```
pip3 install -r requirements.txt
```


## Create Database inside the postgres using the below commands

```
sudo -u postgres psql
```
```
create database ku8eitout;
```
```
create user admin with password 'admin';
```
```
grant all privleges on database ku8eitout to admin;
```

## Again execute the below commands inside the flask terminal
```
flask db init
```
```
flask db migrate
```
```
flask db upgrade
```

## Add the configurations inside the pycharm and run the project
'''
Set the python interpreter of the Pycharm to the working directory /home/sankalp_saxena/Desktop/ku8e-it-out/venv/bin
'''
=======
# py-flask
A website using python , postgres and FLask for backend.
>>>>>>> 29c73c2c1825578c2016f8f83b34e0e80f0d8707
