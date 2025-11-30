from DAO.conexion import Conexion
from DTO.proyectoDto import ProyectoDTO
from DAO.baseDao import DaoBase

class ProyectoDAO(DaoBase):
    def __init__(self):
        self.conexion = Conexion()

    def crear(self, proyecto: ProyectoDTO):
        conn = self.conexion.conectar()
        if not conn:
            return False
        cursor = conn.cursor()
        sql = "INSERT INTO proyectos (nombre, descripcion, fecha_inicio) VALUES (%s, %s, %s)"
        valores = (proyecto.nombre, proyecto.descripcion, proyecto.fecha_inicio)
        try:
            cursor.execute(sql, valores)
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al agregar proyecto: {e}")
            return False
        finally:
            self.conexion.desconectar()

    def listar(self):
        conn = self.conexion.conectar()
        if not conn:
            return []
        cursor = conn.cursor()
        sql = "SELECT * FROM proyectos"
        cursor.execute(sql)
        rows = cursor.fetchall()
        self.conexion.desconectar()
        
        proyectos = []
        for r in rows:
            # Asumiendo el orden: id, nombre, descripcion, fecha_inicio
            # Ajustar índices si la tabla tiene otra estructura, pero basado en el insert parece correcto
            proy = ProyectoDTO(id=r[0], nombre=r[1], descripcion=r[2], fecha_inicio=r[3])
            proyectos.append(proy)
        return proyectos

    def buscar_por_id(self, id):
        conn = self.conexion.conectar()
        if not conn:
            return None
        cursor = conn.cursor()
        sql = "SELECT * FROM proyectos WHERE id = %s"
        cursor.execute(sql, (id,))
        r = cursor.fetchone()
        self.conexion.desconectar()
        
        if not r:
            return None
            
        return ProyectoDTO(id=r[0], nombre=r[1], descripcion=r[2], fecha_inicio=r[3])

    def actualizar(self, proyecto: ProyectoDTO):
        conn = self.conexion.conectar()
        if not conn:
            return False
        cursor = conn.cursor()
        sql = "UPDATE proyectos SET nombre = %s, descripcion = %s, fecha_inicio = %s WHERE id = %s"
        valores = (proyecto.nombre, proyecto.descripcion, proyecto.fecha_inicio, proyecto.id)
        try:
            cursor.execute(sql, valores)
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar proyecto: {e}")
            return False
        finally:
            self.conexion.desconectar()

    def eliminar(self, id):
        conn = self.conexion.conectar()
        if not conn:
            return False
        cursor = conn.cursor()
        sql = "DELETE FROM proyectos WHERE id = %s"
        try:
            cursor.execute(sql, (id,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar proyecto: {e}")
            return False
        finally:
            self.conexion.desconectar()
