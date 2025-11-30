class ProyectoDTO:
    def __init__(self, id=None, nombre=None, descripcion=None, fecha_inicio=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio

    def __str__(self):
        return f'ProyectoDTO(id={self.id}, nombre={self.nombre}, fecha_inicio={self.fecha_inicio})'
