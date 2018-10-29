La base de datos es postgres, es una aplicación hecha en flask.

Para cargar los scripts en la base de datos:

?  psql  -h [host] -U [user] -d [basename]  -f  [script_to_load]

Para sacar un script de la base de datos:

pg_dump --no-acl --no-owner -h [host ip].compute-1.amazonaws.com -U [user name] -t [table name] --data-only [database name] > table.dump

Para correr la aplicación localmente se debe correr el script 

./create_databbase

Esto creará un contenedor de docker con la base de datos y las credenciales especificadas.

Luego cargar los scripts con los datos necesarios [Contactar a jorge].


