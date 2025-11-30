class UsuarioDTO:
    def __init__(self, id, username, password_hash, rol='user', empleado_id=None):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.rol = rol
        self.empleado_id = empleado_id