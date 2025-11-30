from DAO.conexion import Conexion
from DTO.empleadoDto import EmpleadoDTO
from DAO.baseDao import DaoBase

class EmpleadoDAO(DaoBase):
    def __init__(self):
        self.conexion = Conexion()

    # ========== Crear (Polimorfismo) ==========
    def crear(self, empleado: EmpleadoDTO):
        conn = self.conexion.conectar()
        if not conn:
            return False
        
        cursor = conn.cursor()
        sql = """
            INSERT INTO empleados 
            (nombre, apellido, direccion, telefono, email, fecha_inicio, salario, departamento_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (
            empleado.nombre, empleado.apellido, empleado.direccion, empleado.telefono,
            empleado.email, empleado.fecha_inicio, empleado.salario, empleado.departamento_id
        )

        try:
            cursor.execute(sql, valores)
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al agregar empleado: {e}")
            return False
        finally:
            self.conexion.desconectar()

    # ========== Listar (Polimorfismo) ==========
    def listar(self):
        conn = self.conexion.conectar()
        if not conn:
            return []

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM empleados")
        rows = cursor.fetchall()

        empleados = []
        for r in rows:
            emp = EmpleadoDTO(
                id=r[0], nombre=r[1], apellido=r[2], direccion=r[3], telefono=r[4],
                email=r[5], fecha_inicio=r[6], salario=r[7], departamento_id=r[8]
            )
            empleados.append(emp)

        self.conexion.desconectar()
        return empleados

    # ========== Buscar ==========
    def buscar_por_id(self, id):
        conn = self.conexion.conectar()
        if not conn:
            return None

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM empleados WHERE id = %s", (id,))
        r = cursor.fetchone()

        self.conexion.desconectar()

        if not r:
            return None

        return EmpleadoDTO(
            id=r[0], nombre=r[1], apellido=r[2], direccion=r[3], telefono=r[4],
            email=r[5], fecha_inicio=r[6], salario=r[7], departamento_id=r[8]
        )

    # ========== Actualizar (Polimorfismo) ==========
    def actualizar(self, empleado: EmpleadoDTO):
        conn = self.conexion.conectar()
        if not conn:
            return False

        cursor = conn.cursor()
        sql = """
            UPDATE empleados SET 
            nombre = %s, apellido = %s, direccion = %s, telefono = %s, email = %s,
            fecha_inicio = %s, salario = %s, departamento_id = %s
            WHERE id = %s
        """

        valores = (
            empleado.nombre, empleado.apellido, empleado.direccion, empleado.telefono,
            empleado.email, empleado.fecha_inicio, empleado.salario,
            empleado.departamento_id, empleado.id
        )

        try:
            cursor.execute(sql, valores)
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar empleado: {e}")
            return False
        finally:
            self.conexion.desconectar()

    # ========== Eliminar (Polimorfismo) ==========
    def eliminar(self, id):
        conn = self.conexion.conectar()
        if not conn:
            return False
        
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM empleados WHERE id=%s", (id,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar empleado: {e}")
            return False
        finally:
            self.conexion.desconectar()

    # ========== Buscar por departamento ==========
    def buscar_por_departamento(self, departamento_id):
        conn = self.conexion.conectar()
        if not conn:
            return []

        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM empleados WHERE departamento_id = %s",
            (departamento_id,)
        )
        rows = cursor.fetchall()

        self.conexion.desconectar()

        empleados = []
        for r in rows:
            emp = EmpleadoDTO(
                id=r[0], nombre=r[1], apellido=r[2], direccion=r[3], telefono=r[4],
                email=r[5], fecha_inicio=r[6], salario=r[7], departamento_id=r[8]
            )
            empleados.append(emp)

        return empleados
