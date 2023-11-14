from sqlalchemy import create_engine
def lambda_handler(id_clase, context):
# Config
    connection_string = f'mysql+pymysql://{user}:{password}@{host}/{db}'
    connection = create_engine(connection_string)
    Session = connection.connect()
    try:
#asistentes totales
        attendees_count = Session.execute(text("SELECT COUNT(*) FROM attendee WHERE class_id = :class_id"),{'class_id': id_clase}).scalar()
#registrados totales
        registrants_count = Session.execute(text("SELECT COUNT(*) FROM registrants WHERE class_id = :class_id"),{'class_id': id_clase}).scalar()
#porcentaje de asistencia  
        attendance_percentage = (attendees_count / registrants_count * 100) if registrants_count else 0

        response = {
            'id_clase': id_clase,
            'numero_de_asistentes': attendees_count,
            'numero_de_registrados': registrants_count,
            'porcentaje_de_asistencia': attendance_percentage
        }
        return response
    except Exception as e:
        print(f"Error al procesar la consulta: {e}")
        return {
            'statusCode': 500,
            'body': 'Ocurrió un error al procesar la consulta'
        }
    finally:
        session.close()