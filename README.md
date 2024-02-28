Dados Web - API
====================

## Requerimientos

* Python 3.11+
* Pip 3+
* MySQL

## Setup Inicial

1. Crear Ambiente Virtual con Python `virtualenv`

2. Clonar el Proyecto

3. Activar el Ambiente Virtual
Linux: `$ source env/bin/activate`
Windows: `C:/path_to_the_folder/ > .\venv-name\Scripts\activate`

4. Ingresar al Directorio Raíz

5. Instalar las Librerías Requeridas
`$ pip install -r requirements.txt`

6. Crear la Base de Datos en MySQL con el Nombre Establecido en `my.cnf`

6. Aplicar las Migraciones de Django
`$ python3 manage.py makemigrations core`
`$ python3 manage.py migrate`

7. Correr el Servidor
 `$ python3 manage.py runserver`
