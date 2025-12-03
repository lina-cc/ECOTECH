import os
import datetime
import stdiomask
import requests
from DAO.usuarioDao import UsuarioDAO
from DAO.historialDao import HistorialDAO
from DTO.historialDto import HistorialDTO
from DTO.usuarioDto import UsuarioDTO

def clear():
    # funcion para limpiar la pantalla dependiendo del sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    # instanciamos el dao de usuario
    dao = UsuarioDAO()
    intentos = 0
    # permitimos hasta 3 intentos de login
    while intentos < 3:
        clear()
        print("=== LOGIN ECOTECH ===")
        username = input("Usuario: ")
        # usamos stdiomask para ocultar la contraseña al escribir
        password = stdiomask.getpass(prompt="Contraseña: ", mask="*") # Ocultar password
        
        # intentamos autenticar con el dao
        user_dto = dao.autenticar(username, password)
        if user_dto:
            print(f"Bienvenido {user_dto.username} ({user_dto.rol})")
            return user_dto
        else:
            print("Credenciales incorrectas.")
            intentos += 1
            input("Presione Enter para intentar de nuevo...")
    
    print("Demasiados intentos fallidos. Saliendo...")
    return None

def menu_gestion_usuarios(usuario_actual):
    if usuario_actual.rol != 'admin':
        print("Acceso denegado. Solo administradores.")
        input("Enter...")
        return

    dao = UsuarioDAO()
    while True:
        clear()
        print("=== GESTIÓN DE USUARIOS ===")
        print("1. Listar Usuarios")
        print("2. Crear Usuario")
        print("3. Eliminar Usuario")
        print("0. Volver")
        op = input("Opción: ")
        
        if op == "0": break
        elif op == "1":
            usuarios = dao.listar()
            print(f"\n{'ID':<5} | {'USERNAME':<20} | {'ROL':<10}")
            print("-" * 40)
            for u in usuarios:
                print(f"{u.id:<5} | {u.username:<20} | {u.rol:<10}")
            input("\nEnter para continuar...")
        elif op == "2":
            print("\n--- Nuevo Usuario ---")
            username = input("Username: ")
            password = stdiomask.getpass(prompt="Password: ", mask="*")
            rol = input("Rol (admin/user) [Default: user]: ")
            if not rol:
                rol = 'user'
            nuevo = UsuarioDTO(None, username, password, rol)
            if dao.crear(nuevo):
                print("Usuario creado exitosamente.")
            else:
                print("Error al crear usuario.")
            input("Enter...")
        elif op == "3":
            print("\n--- Eliminar Usuario ---")
            try:
                id_usuario = int(input("ID del usuario a eliminar: "))
                if dao.eliminar(id_usuario):
                    print("Usuario eliminado exitosamente.")
                else:
                    print("Error al eliminar usuario.")
            except ValueError:
                print("ID inválido.")
            input("Enter...")

def obtener_indicador_api(indicador, fecha=None):
    # url base de la api mindicador.cl
    base_url = "https://mindicador.cl/api"
    # construimos la url con el indicador solicitado
    url = f"{base_url}/{indicador}"
    # si se especifica una fecha, la agregamos a la url
    if fecha:
        url += f"/{fecha}"

    try:
        # realizamos la petición get a la api
        response = requests.get(url)
        # verificamos si hubo error en la respuesta http
        response.raise_for_status()
        # convertimos la respuesta a json
        data = response.json()

        if fecha:
            # si pedimos fecha especifica, buscamos en la serie
            if 'serie' in data and len(data['serie']) > 0:
                valor = data['serie'][0]['valor']
                fecha_valor = data['serie'][0]['fecha']
                return {'valor': valor, 'fecha': fecha_valor}
        else:
            # si no hay fecha, tomamos el valor más reciente
            if 'serie' in data and len(data['serie']) > 0:
                    valor = data['serie'][0]['valor']
                    fecha_valor = data['serie'][0]['fecha']
                    return {'valor': valor, 'fecha': fecha_valor}
        return None
    except Exception as e:
        print(f"Error al consultar API: {e}")
        return None

def obtener_rango_indicador(indicador, fecha_inicio, fecha_fin):
    # url base para consultas por año
    base_url = "https://mindicador.cl/api"
    resultados = []
    
    start_year = fecha_inicio.year
    end_year = fecha_fin.year
    
    # iteramos por cada año en el rango solicitado
    for year in range(start_year, end_year + 1):
        url = f"{base_url}/{indicador}/{year}"
        try:
            # consultamos la api para ese año
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if 'serie' in data:
                # recorremos los valores devueltos
                for item in data['serie']:
                    fecha_item_iso = item['fecha']
                    # convertimos la fecha de string a objeto date
                    fecha_item = datetime.datetime.strptime(fecha_item_iso[:10], '%Y-%m-%d').date()
                    
                    # filtramos solo las fechas que están dentro del rango exacto
                    if fecha_inicio <= fecha_item <= fecha_fin:
                        resultados.append({
                            'fecha': fecha_item,
                            'valor': item['valor']
                        })
        except Exception as e:
            print(f"Error al consultar año {year}: {e}")
            
    # ordenamos los resultados por fecha ascendente
    resultados.sort(key=lambda x: x['fecha'])
    return resultados

def menu_gestor_financiero(usuario_actual):
    historial_dao = HistorialDAO()
    
    while True:
        clear()
        print(f"=== GESTOR FINANCIERO (Usuario: {usuario_actual.username}) ===")
        print("1. Consultar Indicadores")
        print("2. Ver Historial de Consultas")
        print("0. Volver")
        
        op = input("Opción: ")
        
        if op == "0": break
        elif op == "1":
            print("\nIndicadores disponibles: uf, ivp, dolar, euro, ipc, utm")
            indicador = input("Ingrese indicador a consultar: ").lower()
            
            print("\nTipo de consulta:")
            print("1. Fecha específica")
            print("2. Periodo (Rango de fechas)")
            tipo = input("Seleccione opción: ")
            
            if tipo == "1":
                fecha_str = input("Fecha (dd-mm-yyyy) [Enter para hoy]: ")
                fecha = fecha_str if fecha_str else None
                
                resultado = obtener_indicador_api(indicador, fecha)
                
                if resultado:
                    print(f"\nValor {indicador.upper()}: {resultado['valor']}")
                    print(f"Fecha: {resultado['fecha']}")
                    
                    try:
                        fecha_valor_iso = resultado['fecha']
                        fecha_valor_dt = datetime.datetime.strptime(fecha_valor_iso[:10], '%Y-%m-%d')
                        fecha_valor = fecha_valor_dt.strftime('%Y-%m-%d')
                    except:
                        fecha_valor = datetime.date.today()

                    nuevo_historial = HistorialDTO(
                        None, indicador, resultado['valor'], fecha_valor, None, "mindicador.cl", usuario_actual.id
                    )
                    if historial_dao.agregar_consulta(nuevo_historial):
                        print("Consulta registrada en historial.")
                    else:
                        print("Error al registrar historial.")
                else:
                    print("No se pudo obtener el indicador.")
            
            elif tipo == "2":
                try:
                    f_inicio_str = input("Fecha Inicio (dd-mm-yyyy): ")
                    f_fin_str = input("Fecha Fin (dd-mm-yyyy): ")
                    
                    f_inicio = datetime.datetime.strptime(f_inicio_str, '%d-%m-%Y').date()
                    f_fin = datetime.datetime.strptime(f_fin_str, '%d-%m-%Y').date()
                    
                    if f_inicio > f_fin:
                        print("Error: Fecha inicio mayor a fecha fin.")
                    elif (f_fin.year - f_inicio.year) > 5:
                         print("Error: El rango no puede exceder los 5 años.")
                    else:
                        print("\nConsultando...")
                        resultados = obtener_rango_indicador(indicador, f_inicio, f_fin)
                        
                        if resultados:
                            print(f"\nResultados para {indicador.upper()} ({f_inicio} al {f_fin}):")
                            print(f"{'FECHA':<15} | {'VALOR':<10}")
                            print("-" * 30)
                            for r in resultados:
                                print(f"{r['fecha']} | {r['valor']}")
                        else:
                            print("No se encontraron datos para el rango seleccionado.")
                except ValueError:
                    print("Formato de fecha incorrecto. Use dd-mm-yyyy.")
            
            input("\nEnter para continuar...")
            
        elif op == "2":
            if usuario_actual.rol == 'admin':
                lista = historial_dao.listar_consultas()
                print(f"\n{'ID':<5} | {'USUARIO ID':<10} | {'IND':<10} | {'VALOR':<10} | {'FECHA'}")
            else:
                lista = historial_dao.listar_por_usuario(usuario_actual.id)
                print(f"\n{'ID':<5} | {'IND':<10} | {'VALOR':<10} | {'FECHA'}")
            
            print("-" * 60)
            for h in lista:
                if usuario_actual.rol == 'admin':
                    print(f"{h.id:<5} | {h.usuario_id:<10} | {h.indicador:<10} | {h.valor:<10} | {h.fecha_consulta}")
                else:
                    print(f"{h.id:<5} | {h.indicador:<10} | {h.valor:<10} | {h.fecha_consulta}")
            input("\nEnter para continuar...")

def main():
    usuario_actual = login()
    if not usuario_actual:
        return

    while True:
        clear()
        print(f"=== MENÚ PRINCIPAL ECOTECH ===")
        print("1. Gestión de Usuarios")
        print("2. Gestor Financiero")
        print("0. Salir")
        
        opcion = input("Seleccione opción: ")
        
        if opcion == "1":
            menu_gestion_usuarios(usuario_actual)
        elif opcion == "2":
            menu_gestor_financiero(usuario_actual)
        elif opcion == "0":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
