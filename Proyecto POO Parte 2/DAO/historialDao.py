from DAO.conexion import Conexion
from DTO.historialDto import HistorialDTO

class HistorialDAO:
    def __init__(self):
        self.conexion = Conexion()

    def agregar_consulta(self, historial: HistorialDTO):
        conn = self.conexion.conectar()
        if not conn:
            return False
        cursor = conn.cursor()
        sql = """
            INSERT INTO historial_consultas (indicador, valor, fecha_valor, origen, usuario_id)
            VALUES (%s, %s, %s, %s, %s)
        """
        # Nota: fecha_consulta es default CURRENT_TIMESTAMP en BD, no necesitamos enviarla si no queremos
        valores = (historial.indicador, historial.valor, historial.fecha_valor, historial.origen, historial.usuario_id)
        try:
            cursor.execute(sql, valores)
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al guardar historial: {e}")
            return False
        finally:
            self.conexion.desconectar()

    def listar_consultas(self):
        conn = self.conexion.conectar()
        if not conn:
            return []
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM historial_consultas ORDER BY fecha_consulta DESC"
        cursor.execute(sql)
        datos = cursor.fetchall()
        self.conexion.desconectar()
        resultados = []
        for d in datos:
            resultados.append(HistorialDTO(
                d['id'], d['indicador'], d['valor'], d['fecha_valor'], 
                d['fecha_consulta'], d['origen'], d['usuario_id']
            ))
        return resultados

    def listar_por_usuario(self, usuario_id):
        conn = self.conexion.conectar()
        if not conn:
            return []
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM historial_consultas WHERE usuario_id = %s ORDER BY fecha_consulta DESC"
        cursor.execute(sql, (usuario_id,))
        datos = cursor.fetchall()
        self.conexion.desconectar()
        resultados = []
        for d in datos:
            resultados.append(HistorialDTO(
                d['id'], d['indicador'], d['valor'], d['fecha_valor'], 
                d['fecha_consulta'], d['origen'], d['usuario_id']
            ))
        return resultados
