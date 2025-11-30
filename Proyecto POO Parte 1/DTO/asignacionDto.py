class AsignacionDTO:
    def __init__(self, id=None, empleado_id=None, proyecto_id=None):
        self.id = id
        self.empleado_id = empleado_id
        self.proyecto_id = proyecto_id

    def __str__(self):
        return f'AsignacionDTO(id={self.id}, empleado_id={self.empleado_id}, proyecto_id={self.proyecto_id})'
