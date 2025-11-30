class HistorialDTO:
    def __init__(self, id, indicador, valor, fecha_valor, fecha_consulta, origen, usuario_id):
        self.id = id
        self.indicador = indicador
        self.valor = valor
        self.fecha_valor = fecha_valor
        self.fecha_consulta = fecha_consulta
        self.origen = origen
        self.usuario_id = usuario_id
