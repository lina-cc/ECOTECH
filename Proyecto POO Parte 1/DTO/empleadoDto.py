from DTO.personaDto import Persona

class EmpleadoDTO:
    def __init__(self, id=None, nombre=None, apellido=None, direccion=None, telefono=None, email=None, fecha_inicio=None, salario=None, departamento_id=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.fecha_inicio = fecha_inicio
        self.salario = salario
        self.departamento_id = departamento_id

    def __str__(self):
        return f'EmpleadoDTO(id={self.id}, nombre={self.nombre}, apellido={self.apellido}, departamento_id={self.departamento_id})'

class EmpleadoDto(Persona):
    def __init__(self, id, nombre, apellido, direccion, telefono, email,
                 fecha_inicio, salario, departamento_id):
        
        super().__init__(nombre, apellido, direccion, telefono, email)
        
        self.id = id
        self.fecha_inicio = fecha_inicio
        self.salario = salario
        self.departamento_id = departamento_id

    # Polimorfismo con override
    def mostrar_info(self):
        return f"Empleado: {self.nombre} {self.apellido} | Salario: {self.salario}"