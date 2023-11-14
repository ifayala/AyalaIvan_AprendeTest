import boto3
import pandas as pd
from sqlalchemy import create_engine

def process_csv(file_body):
    # Leemos el contenido en un DataFrame de pandas
    df = pd.read_csv(file_body)
    return df

def create_summary_table(clases_df, registrants_df, attendee_df):
#renombro columnas
    clases_df.rename(columns={'id': 'class_id'}, inplace=True)
    registrants_df.rename(columns={'class_id': 'class_id_reg', 'email_attendee': 'email'}, inplace=True)
    attendees_df.rename(columns={'class_id': 'class_id_att', 'email_attendee': 'email'}, inplace=True)
#unimos dfs
    summary_df = pd.merge(clases_df, registrants_df, left_on='class_id', right_on='class_id_reg', how='left')
    summary_df = pd.merge(summary_df, attendees_df, left_on=['class_id', 'email'], right_on=['class_id_att', 'email'], how='left')
    
# Calculo la duración en segundos
    summary_df['attendee_join_date'] = pd.to_datetime(summary_df['join_time'])
    summary_df['attendee_leave_date'] = pd.to_datetime(summary_df['leave_time'])
    summary_df['attende_seconds_duration'] = (summary_df['attendee_leave_date'] - summary_df['attendee_join_date']).dt.total_seconds()
#Armo df Final
    class_session_df = summary_df[['class_id', 'class_name', 'Docente', 'class_time', 'email', 'registrant_date', 'attendee_join_date', 'attendee_leave_date', 'attende_seconds_duration']].copy()
    class_session_df.rename(columns={'class_id': 'id_clase', 'Docente': 'professor_name', 'class_time': 'fecha_clase'}, inplace=True)
    
    return class_session_df

def lambda_handler(event, context):
# Configurar el cliente S3
    s3_client = boto3.client('s3')
# Obtener los archivos CSV de S3
    bucket_name = 's3://aprende-test/'
    files_prefix = 'AYALA_IVAN/'
    files = ['clases.csv', 'registrants.csv', 'attendee.csv']
# Conexión a la base de datos MySQL
    connection_string = f'mysql+pymysql://{user}:{password}@{host}/{db}'
	connection = create_engine(db_connection_str)
    
    for file in files:
        obj = s3_client.get_object(Bucket=bucket_name, Key=files_prefix + file)
        df = pd.read_csv(obj['Body'])
        df.to_sql(table_name, con=connection, if_exists='append', index=False)
        data_frames[file_name.split('.')[0]] = process_csv(obj['Body'])

#Inserto Tablas RAW
        try:
            cursor.execute(query, values)
            connection.commit()
        except Exception as e:
            print(f"Error al insertar datos: {e}")
            connection.rollback()
            continue

#creo el df sumarizado
	class_session_df = create_summary_table(data_frames['clases'], data_frames['registrants'], data_frames['attendee'])
#inserto
	summary_df.to_sql('class_session', con=connection, if_exists='append', index=False)

    return {
        'statusCode': 200,
        'body': 'Proceso ETL completado con éxito'
    }


