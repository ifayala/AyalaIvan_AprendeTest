# AyalaIvan_AprendeTest

##1.1.

Respuesta es la C, es el servicio de datawarehouse cloud de Amazon Web Services.

##1.2.

Como ventajas diría que son la A y la B ya que solo nos preocupamos por el script que
deseamos ejecutar, la infra la aprovisiona y mantiene automáticamente AWS, y por todo esto
solo se cobra por el tiempo de ejecución del mismo.

##1.3

Hasta donde sé hay 6 tipos de almacenamiento:
-S3 Standard.
-S3 Standard Infrequent Access.
-S3 Standard Infrequent Access (One Zone).
-S3 Glacier.
-S3 Glacier deep archive.
-S3 Intelligent Tiering.
En el ámbito laboral usualmente utilizamos S3 Standard y Glacier luego de cumplido un TTL
para la data.

##2.1,2.3 y 2.4
  
  AyalaIvan_AprendeTest/SQLyBD.sql
  
##2.2
  
  AyalaIvan_AprendeTest/PythonyBD.py
  
##3.1

Amazon SF es el orquestador de workflows serverless que ofrece AWS,
se suele utilizar para secuenciar y ejecutar funciones Lambdas para
automatizar procesos, en el ámbito de data suelen ser procesos ETLs o
bien para deployar modelos de aprendizaje si nos vamos al área de
Datascience.

##3.2

Es el servicio de ETL Autoadministrado de aws por excelencia, ofrece
muchas ventajas para orquestar flujos de transformación y carga de
datos, corre por detrás con EMR y Spark.
Tiene funcionalidades de Data discovery, ya que mapea la metadata de
los archivos (parquet o AVRO) y genera un catálogo con los metadatos
que encuentra, haciendo más fácil la exploración de datos.
Posee auto escalado y se integra con todos los servicios de Data de
AWS : Redshift, RDS, S3, Athena y también con algunas bases de datos
externas.

##3.3

Por la naturaleza de ambos servicios creo que la diferencia radica en
la complejidad de las transformaciones de datos y los volúmenes que
vamos a transformar y cargar.
Para transformaciones y cargas pequeñas de trabajo utilizará Lambdas
combinadas tal vez con SF para orquestación, pero siempre tengo que
tener en cuenta el tiempo máximo de ejecución que ofrece lambda (15
min). Para transformaciones más complejas o volúmenes de datos más
grandes y cargas pesadas de trabajo utilizaría Glue, ya que la
infraestructura sobre la que corre sería la adecuada para estas
condiciones de trabajos.

##4.1 y 4.2
  
  AyalaIvan_AprendeTest/Tables_Creation.py
  
##4.3
  
  AyalaIvan_AprendeTest/lambda_function.py
  
##4.4
  
  ![image](https://github.com/ifayala/AyalaIvan_AprendeTest/assets/51173725/aeb32f5d-ff86-484d-990d-ad89559e251f)
  
##4.5
  
  AyalaIvan_AprendeTest/Bonus.py
