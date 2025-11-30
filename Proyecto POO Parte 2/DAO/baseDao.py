class DaoBase:
    def listar(self):
        raise NotImplementedError("Debes implementar listar() en la clase hija.")

    def crear(self, obj):
        raise NotImplementedError("Debes implementar crear() en la clase hija.")

    def eliminar(self, id):
        raise NotImplementedError("Debes implementar eliminar() en la clase hija.")

    def actualizar(self, obj):
        raise NotImplementedError("Debes implementar actualizar() en la clase hija.")