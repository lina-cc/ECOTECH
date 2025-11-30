class Persona:
    def __init__(self, nombre, apellido, direccion=None, telefono=None, email=None):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    # Método polimórfico
    def mostrar_info(self):
        return f"{self.nombre} {self.apellido}"