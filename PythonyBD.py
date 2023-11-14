import csv
import sqlalchemy
import boto3
from io import StringIO
#Config
db_username = {user}
db_password = {password}
db_host = {db_host}
db_name = {db}
db_port = {puerto}
aws_access_key_id = {access_key_id}
aws_secret_access_key = {secret_access_key}
bucket_name = 's3://aprende-test/'
#Creo Conexion
engine =
sqlalchemy.create_engine(f'postgresql://{db_username}:{db_password}@{
db_host}:{db_port}/{db_name}')
query = '''
SELECT p.name, SUM(v.amount) as total_ventas
FROM Ventas v
INNER JOIN Producto p on v.product_id=p.id
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;
'''
#Run Query
result = engine.execute(query)
#creo el csv
csv_buffer = StringIO()
csv_writer = csv.writer(csv_buffer)
# Escribo los datos en el CSV
csv_writer.writerow(['Name', 'Total Ventas'])#headers
for row in result:
csv_writer.writerow(row)
csv_buffer.seek(0)# Muevo el cursor al inicio del csv en memoria
# Upload a S3 bucket
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id,
aws_secret_access_key=aws_secret_access_key)
s3_client.put_object(Bucket=bucket_name, Key='top_10_products.csv',
Body=csv_buffer.getvalue())