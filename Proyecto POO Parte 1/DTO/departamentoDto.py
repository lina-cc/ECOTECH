class DepartamentoDTO:
    def __init__(self, id=None, nombre=None, gerente=None):
        self.id = id
        self.nombre = nombre
        self.gerente = gerente

    def __str__(self):
        return f'DepartamentoDTO(id={self.id}, nombre={self.nombre}, gerente={self.gerente})'
