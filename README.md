# Guía de implementación del proyecto

## Requisistos Previos

+ [Python 3.9.x](https://www.python.org/downloads/)
+ [VSCode](https://code.visualstudio.com/download)
+ [Oracle XE](https://www.oracle.com/database/technologies/xe-downloads.html)
+ [SQLDeveloper](https://www.oracle.com/tools/downloads/sqldev-downloads.html)

_**Nota:** Para este proyecto se utilizo una version Oracle 18c, disponible hasta la fecha del desarrollo de esta guía_

## Creando nuestro ambiente virtual

Para poder hacer uso de nuestro aplicativo en Django, por recomendación debemos utilizar un entorno virtual en el cual podamos instalar todas las dependencias especificas de este proyecto, evitando asi problemas de compatibilidad con dependencias de otros proyectos.

El primer paso es instalar nuestro ambiente virtual que nos ayudará a almacenar las variables de entorno correspondientes a las dependencias de nuestro proyecto. Esto lo haremos usando el siguiente comando:

```bash
pip3 install virtualenvwrapper-win
```

Una vez instalado, debemos crear nuestro ambiente virtual con el siguiente comando:

```bash
mkvirtualenv portafolio
```
_**Importante:** 'portafolio' corresponde al nombre de nuestro ambiente virtual, que puede usar a conveniencia_

Ya creado, debemos tener en cuenta los siguientes comandos que podrán ser de utilidad:

```bash
workon #lista todos los ambientes virtuales creados
workon nombre_ambiente #Activa el ambiente virtual
deactivate #Desactiva el ambiente virtual(tiene que estar dentro de el)
rmvirtualenv nombre_ambiente #Elimina el ambiente virtual
```

## Preparando nuestro ambiente virtual

Los siguientes últimos pasos consisten en instalar nuestras dependencias dentro de nuestro entorno virtual. En este caso necesitaremos las siguientes:

1. __Django 3.2.7__:

  ```bash
  pip3 install django-admin == x.x
  ```
2. __cx_Oracle__: 
  
  ```bash
  pip3 install cx_Oracle
  ```
## Preparando nuestra base de Datos 

1. Abra el SQLDeveloper y cree una nueva conexión con el usuario System y la contraseña que introdujo al instalar Oracle 18c

2. Ahora hay que crear el siguiente usuario con la siguiente sintaxis:

```SQL
CREATE USER c##Administrador identified by 1234;
GRANT CONNECT, RESOURCE TO c##Administrador;
ALTER USER c##Administrador quota unlimited on USERS;
```
3. Luego vamos a crear una nueva conexión con el usuario y contraseña creados anteriormente.

4. Debe ejecutar los scripts en el siguiente orden:
  1. Ejecutar el Script ‘SCRIPT_BD’
  2. Ejecutar el Script ‘SCRIPT_PROCEDURE_TRIGGER’
  3. Ejecutar el Script ‘SCRIPT_INSERT’

## Últimos Pasos

1. Crear una nueva carpeta en el Escritorio

2. Abrir una terminal dentro de la carpeta

3. Ingresar en nuestro entorno virtual con el comando:

  ```bash
  workon portafolio
  ```

4. Descargar el proyecto con el siguiente comando:

  ```bash
  git clone https://github.com/Vittoowo/Portafolio.git
  ```

5. En la consola, cambiar de directorio a la carpeta Portafolio con el siguiente comando:

  ```bash
  cd Portafolio
  ```
Correr nuestro servidor con el siguiente comando:

  ```bash
  python manage.py runserver
  ```
