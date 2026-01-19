from database import DatabaseConnection
import psycopg2 
from psycopg2 import errors 

def registrar_equipo(modelo, serie, estado="disponible", id_responsable=None):
    """Add a new equipment to the database"""
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
            print(f"Equipment {modelo} registered successfully")
            
        except errors.UniqueViolation:
            conn.rollback()
            print(f"Error: The serial number {serie} is already registered.")
        except errors.ForeignKeyViolation:
            conn.rollback()
            print(f"Error: The responsible ID {id_responsable} does not exist.")        
        except psycopg2.Error as e:
            conn.rollback()
            print(f"Error registering equipment: {e}")
        finally: 
            cursor.close()
            db.disconnect()
            
def listar_equipos():
    """Retrieve all records from the equipment table"""
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
                print(f"Equipment with serial number {serie_equipo} updated.")
            else:
                print(f"Serial number {serie_equipo} not found.")
        except Exception as e:
            conn.rollback()
            print(f"Error: {e}")
        finally:
            db.disconnect()
            
def registrar_responsable(id_emp, emp_name, departamento, email=None):
    """Add a new responsible person to the database"""
    db = DatabaseConnection()
    conn = db.connect()
    if conn:
        try:
            cursor = conn.cursor()
            # Usamos %s para que sea seguro contra Inyección SQL
            query = "INSERT INTO empleados (id_emp, emp_name, departamento, email) VALUES (%s, %s, %s, %s);"
            cursor.execute(query, (id_emp, emp_name, departamento, email))
            conn.commit()
            print(f"Responsible '{emp_name}' registered successfully.")
        except psycopg2.Error as e:
            conn.rollback()
            print(f"Error registering responsible: {e}")
        finally:
            if 'cursor' in locals(): cursor.close()
            db.disconnect()

def listar_responsables():
    """Retrieve all registered responsible persons"""
    db = DatabaseConnection()
    conn = db.connect()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT id_emp, emp_name, departamento FROM empleados;"
            cursor.execute(query)
            return cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Error consulting responsible persons: {e}")
            return []
        finally:
            if 'cursor' in locals(): cursor.close()
            db.disconnect()