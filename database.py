import psycopg2
from psycopg2 import Error

class DatabaseConnection:
    def __init__(self):
        self.host = "localhost"
        self.port = "5432"
        self.user = "postgres"
        self.password = ""
        self.database = "it_inventory"
        self.connection = None 
    
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return self.connection 
        except Error as e:
            print(f"Error {e}")
            return None
    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")
        
