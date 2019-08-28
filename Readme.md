La base de datos es postgres, es una aplicación hecha en flask.

Para cargar los scripts en la base de datos:

?  psql  -h [host] -U [user] -d [basename]  -f  [script_to_load]

Para sacar un script de la base de datos:

pg_dump --no-acl --no-owner -h [host ip].compute-1.amazonaws.com -U [user name] -t [table name] --data-only [database name] > table.dump

Para correr la aplicación únicamente debes correr este comando:

 docker-compose up --build -d
 
 Eso creará dos contenedores, uno de base de datos y otro de la aplicación.
 
 Al correr: 
 
 docker-compose down
 
 Los contenedores serán eliminados.

Luego cargar los scripts con los datos necesarios [Contactar a jorge].


Para correr la aplicación localmente (sin docker) se debe correr el script 
(debes cambiar el string de conexion de la base de datos, ya que por defecto se unirá al contenedor)
sh create_database
export FLASK_ENV=development
export FLASK_APP=run.py
run flask

Esto creará un contenedor de docker con la base de datos y las credenciales especificadas.

Si quieres entrar al contenedor, en el terminal ejecuta lo siguiente:
docker exec -it id_del_container /bin/sh
Una vez dentro, ejecutar:
psql -U postgres
\c mybase


