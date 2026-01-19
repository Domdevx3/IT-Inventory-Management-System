from database import DatabaseConnection
import psycopg2 
from psycopg2 import errors 

def registrar_equipo(modelo, serie, estado="disponible", id_responsable=None):
    """Inserta un nuevo activo en la tabla de equipos"""
    db = DatabaseConnection()
    conn = db.connect()
    
    if conn:
        try:
            cursor = conn.cursor()
            #Consulta parametrizada
            query = """INSERT INTO equipos (modelo, num_serie, estado, id_responsable) VALUES (%s, %s, %s, %s);"""
            
            datos = (modelo, serie, estado, id_responsable)
            
            cursor.execute(query, datos)
            conn.commit() 
            print(f"Equipo {modelo} registrado con éxito")
            
        except errors.UniqueViolation:
            conn.rollback()
            print(f"Error: El número de serie {serie} ya está registrado.")
        except errors.ForeignKeyViolation:
            conn.rollback()
            print(f"Error: El ID de responsable {id_responsable} no existe.")        
        except psycopg2.Error as e:
            conn.rollback()
            print(f"Error al registrar equipo: {e}")
        finally: 
            cursor.close()
            db.disconnect()
            
def listar_equipos():
    """Recupera todos los registros de la tabla equipos"""
    db = DatabaseConnection()
    conn = db.connect()
    
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT id_equipos, modelo, num_serie, estado, id_responsable FROM equipos;"
            cursor.execute(query)
            
            resultados = cursor.fetchall()
            return resultados
        except psycopg2.Error as e:
            print(f"Error al consultar datos: {e}")
            return []
        finally:
            if 'cursor' in locals(): cursor.close()
            db.disconnect()
            
def actualizar_estado_por_serie(serie_equipo, nuevo_estado):
    db = DatabaseConnection()
    conn = db.connect()
    if conn:
        try:
            cursor = conn.cursor()
            estado_limpio = nuevo_estado.lower().strip()
            # Cambiamos WHERE id_equipo por WHERE num_serie
            query = "UPDATE equipos SET estado = %s WHERE num_serie = %s;"
            
            cursor.execute(query, (estado_limpio, serie_equipo))
            
            if cursor.rowcount > 0:
                conn.commit()
                print(f"Equipo con serie {serie_equipo} actualizado.")
            else:
                print(f"No se encontró la serie {serie_equipo}.")
        except Exception as e:
            conn.rollback()
            print(f"Error: {e}")
        finally:
            db.disconnect()