from DAO.conexion import Conexion
from DTO.asignacionDto import AsignacionDTO
from DAO.baseDao import DaoBase

class AsignacionDAO(DaoBase):
    def __init__(self):
        self.conexion = Conexion()

    def crear(self, asignacion: AsignacionDTO):
        conn = self.conexion.conectar()
        if not conn:
            return False
        cursor = conn.cursor()
        sql = "INSERT INTO asignacion_empleados_proyectos (empleado_id, proyecto_id) VALUES (%s, %s)"
        valores = (asignacion.empleado_id, asignacion.proyecto_id)
        try:
            cursor.execute(sql, valores)
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al agregar asignación: {e}")
            return False
        finally:
            self.conexion.desconectar()

    def listar(self):
        conn = self.conexion.conectar()
        if not conn:
            return []
        cursor = conn.cursor()
        sql = """
        SELECT a.id, a.empleado_id, a.proyecto_id
        FROM asignacion_empleados_proyectos a
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        self.conexion.desconectar()
        
        asignaciones = []
        for r in rows:
            # id, empleado_id, proyecto_id
            asig = AsignacionDTO(id=r[0], empleado_id=r[1], proyecto_id=r[2])
            asignaciones.append(asig)
        return asignaciones

    def buscar_por_id(self, id):
        conn = self.conexion.conectar()
        if not conn:
            return None
        cursor = conn.cursor()
        sql = "SELECT * FROM asignacion_empleados_proyectos WHERE id = %s"
        cursor.execute(sql, (id,))
        r = cursor.fetchone()
        self.conexion.desconectar()
        
        if not r:
            return None
            
        # Asumiendo que la tabla tiene id, empleado_id, proyecto_id en ese orden o similar
        # El fetchone devuelve una tupla.
        return AsignacionDTO(id=r[0], empleado_id=r[1], proyecto_id=r[2])

    def eliminar(self, id):
        conn = self.conexion.conectar()
        if not conn:
            return False
        cursor = conn.cursor()
        sql = "DELETE FROM asignacion_empleados_proyectos WHERE id = %s"
        try:
            cursor.execute(sql, (id,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar asignación: {e}")
            return False
        finally:
            self.conexion.desconectar()

    def actualizar(self, obj):
        # Asignacion no tiene update en el menu original, pero por cumplir interfaz base:
        raise NotImplementedError("Actualizar no implementado para Asignacion")
