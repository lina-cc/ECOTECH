class RegistroTiempoDTO:
    def __init__(self, id=None, empleado_id=None, proyecto_id=None, fecha=None, horas_trabajadas=None, descripcion=None):
        self.id = id
        self.empleado_id = empleado_id
        self.proyecto_id = proyecto_id
        self.fecha = fecha
        self.horas_trabajadas = horas_trabajadas
        self.descripcion = descripcion

    def __str__(self):
        return f'RegistroTiempoDTO(id={self.id}, empleado_id={self.empleado_id}, proyecto_id={self.proyecto_id}, fecha={self.fecha}, horas={self.horas_trabajadas})'
