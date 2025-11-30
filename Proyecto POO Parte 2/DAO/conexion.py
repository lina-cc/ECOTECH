import mysql.connector
from mysql.connector import Error

class Conexion:
    def __init__(self):
        self.host = "localhost"
        self.user = "ecotech_user"
        self.password = "ecotech123"
        self.port = '3306'
        self.database = "base"
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
                database=self.database
            )
            if self.conexion.is_connected():
                return self.conexion
        except Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            return None

    def desconectar(self):
        if self.conexion.is_connected():
            self.conexion.close()
