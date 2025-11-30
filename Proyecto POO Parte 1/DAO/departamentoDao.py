from DAO.conexion import Conexion
from DTO.departamentoDto import DepartamentoDTO
from DAO.baseDao import DaoBase

class DepartamentoDAO(DaoBase):
    def __init__(self):
        self.conexion = Conexion()

    def crear(self, departamento: DepartamentoDTO):
        conn = self.conexion.conectar()
        if not conn:
            return False
        cursor = conn.cursor()
        sql = "INSERT INTO departamentos (nombre, gerente) VALUES (%s, %s)"
        valores = (departamento.nombre, departamento.gerente)
        try:
            cursor.execute(sql, valores)
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al agregar departamento: {e}")
            return False
        finally:
            self.conexion.desconectar()

    def listar(self):
        conn = self.conexion.conectar()
        if not conn:
            return []
        cursor = conn.cursor()
        sql = "SELECT * FROM departamentos"
        cursor.execute(sql)
        rows = cursor.fetchall()
        self.conexion.desconectar()
        
        departamentos = []
        for r in rows:
            # id, nombre, gerente
            dept = DepartamentoDTO(id=r[0], nombre=r[1], gerente=r[2])
            departamentos.append(dept)
        return departamentos

    def buscar_por_id(self, id):
        conn = self.conexion.conectar()
        if not conn:
            return None
        cursor = conn.cursor()
        sql = "SELECT * FROM departamentos WHERE id = %s"
        cursor.execute(sql, (id,))
        r = cursor.fetchone()
        self.conexion.desconectar()
        
        if not r:
            return None
        
        return DepartamentoDTO(id=r[0], nombre=r[1], gerente=r[2])

    def actualizar(self, departamento: DepartamentoDTO):
        conn = self.conexion.conectar()
        if not conn:
            return False
        cursor = conn.cursor()
        sql = "UPDATE departamentos SET nombre = %s, gerente = %s WHERE id = %s"
        valores = (departamento.nombre, departamento.gerente, departamento.id)
        try:
            cursor.execute(sql, valores)
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar departamento: {e}")
            return False
        finally:
            self.conexion.desconectar()

    def eliminar(self, id):
        conn = self.conexion.conectar()
        if not conn:
            return False
        cursor = conn.cursor()
        sql = "DELETE FROM departamentos WHERE id = %s"
        try:
            cursor.execute(sql, (id,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar departamento: {e}")
            return False
        finally:
            self.conexion.desconectar()

