from DAO.conexion import Conexion
from DAO.baseDao import DaoBase
from DTO.usuarioDto import UsuarioDTO
import bcrypt

class UsuarioDAO(DaoBase):
    def __init__(self):
        self.conexion = Conexion()

    def autenticar(self, username, password):
        conn = self.conexion.conectar()
        if not conn:
            return None
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM usuarios WHERE username = %s"
        cursor.execute(sql, (username,))
        usuario_data = cursor.fetchone()
        self.conexion.desconectar()

        if usuario_data:
            # Verificar contraseña con bcrypt
            # Nota: password_hash en BD debe ser el hash generado por bcrypt
            if bcrypt.checkpw(password.encode('utf-8'), usuario_data['password_hash'].encode('utf-8')):
                return UsuarioDTO(
                    usuario_data['id'],
                    usuario_data['username'],
                    usuario_data['password_hash'],
                    usuario_data['rol'],
                    usuario_data['empleado_id']
                )
        return None

    def crear(self, usuario: UsuarioDTO):
        # Hashear password antes de guardar
        hashed = bcrypt.hashpw(usuario.password_hash.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        conn = self.conexion.conectar()
        if not conn:
            return False
        cursor = conn.cursor()
        sql = "INSERT INTO usuarios (username, password_hash, rol, empleado_id) VALUES (%s, %s, %s, %s)"
        valores = (usuario.username, hashed, usuario.rol, usuario.empleado_id)
        try:
            cursor.execute(sql, valores)
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            return False
        finally:
            self.conexion.desconectar()

    def listar(self):
        conn = self.conexion.conectar()
        if not conn:
            return []
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM usuarios"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        self.conexion.desconectar()
        usuarios = []
        for r in resultados:
            usuarios.append(UsuarioDTO(
                r['id'], r['username'], r['password_hash'], r['rol'], r['empleado_id']
            ))
        return usuarios

    def eliminar(self, id):
        if id == 2:
            print("Error: No se puede eliminar al usuario administrador principal.")
            return False
        conn = self.conexion.conectar()
        if not conn:
            return False
        cursor = conn.cursor()
        sql = "DELETE FROM usuarios WHERE id = %s"
        try:
            cursor.execute(sql, (id,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            return False
        finally:
            self.conexion.desconectar()