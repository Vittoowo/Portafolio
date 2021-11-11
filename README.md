# Guía de implementación del proyecto

## Requisistos Previos

+ [Python 3.9.x](https://www.python.org/downloads/)
+ [VSCode](https://code.visualstudio.com/download)
+ [Oracle XE](https://www.oracle.com/database/technologies/xe-downloads.html)

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

1. __Django x.x.x__:

  ```bash
  pip3 install django-admin == x.x
  ```
2. __cx_Oracle__: 
  
  ```bash
  pip3 install cx_Oracle
  ```

