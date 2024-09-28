# create database poo_bdd

# create table alumnos (rut varchar(10) primary key not null, nombre varchar(30) not null, edad int not null, mail varchar(30), asignatura varchar(30) not null, promedio float not null);

# pip install -r requirements.txt

# Esta es la estructura del archivo config.py para la conexion a mysql (poner su contraseña de myqsl en password)

DB_CONFIG = {
'host': "localhost",
'user': "root",
'password': "",
'database': "poo_bdd"
};
