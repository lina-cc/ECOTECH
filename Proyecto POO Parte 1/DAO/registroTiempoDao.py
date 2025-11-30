from DAO.conexion import Conexion
from DTO.registroTiempoDto import RegistroTiempoDTO
from DAO.baseDao import DaoBase

class RegistroTiempoDAO(DaoBase):
    def __init__(self):
        self.conexion = Conexion()

    def crear(self, registro: RegistroTiempoDTO):
        conn = self.conexion.conectar()
        if not conn:
            return False
        cursor = conn.cursor()
        sql = """
        INSERT INTO registro_tiempo (empleado_id, proyecto_id, fecha, horas_trabajadas, descripcion)
        VALUES (%s, %s, %s, %s, %s)
        """
        valores = (registro.empleado_id, registro.proyecto_id, registro.fecha, registro.horas_trabajadas, registro.descripcion)
        try:
            cursor.execute(sql, valores)
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al agregar registro de tiempo: {e}")
            return False
        finally:
            self.conexion.desconectar()

    def listar(self):
        conn = self.conexion.conectar()
        if not conn:
            return []
        cursor = conn.cursor()
        sql = "SELECT * FROM registro_tiempo"
        cursor.execute(sql)
        rows = cursor.fetchall()
        self.conexion.desconectar()
        
        registros = []
        for r in rows:
            # id, empleado_id, proyecto_id, fecha, horas_trabajadas, descripcion
            reg = RegistroTiempoDTO(id=r[0], empleado_id=r[1], proyecto_id=r[2], fecha=r[3], horas_trabajadas=r[4], descripcion=r[5])
            registros.append(reg)
        return registros

    def buscar_por_id(self, id):
        conn = self.conexion.conectar()
        if not conn:
            return None
        cursor = conn.cursor()
        sql = "SELECT * FROM registro_tiempo WHERE id = %s"
        cursor.execute(sql, (id,))
        r = cursor.fetchone()
        self.conexion.desconectar()
        
        if not r:
            return None
            
        return RegistroTiempoDTO(id=r[0], empleado_id=r[1], proyecto_id=r[2], fecha=r[3], horas_trabajadas=r[4], descripcion=r[5])

    def actualizar(self, registro: RegistroTiempoDTO):
        conn = self.conexion.conectar()
        if not conn:
            return False
        cursor = conn.cursor()
        sql = """
        UPDATE registro_tiempo
        SET empleado_id = %s, proyecto_id = %s, fecha = %s, horas_trabajadas = %s, descripcion = %s
        WHERE id = %s
        """
        valores = (registro.empleado_id, registro.proyecto_id, registro.fecha, registro.horas_trabajadas, registro.descripcion, registro.id)
        try:
            cursor.execute(sql, valores)
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar registro de tiempo: {e}")
            return False
        finally:
            self.conexion.desconectar()

    def eliminar(self, id):
        conn = self.conexion.conectar()
        if not conn:
            return False
        cursor = conn.cursor()
        sql = "DELETE FROM registro_tiempo WHERE id = %s"
        try:
            cursor.execute(sql, (id,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar registro de tiempo: {e}")
            return False
        finally:
            self.conexion.desconectar()
