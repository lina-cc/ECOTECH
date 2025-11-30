import os
import datetime
import stdiomask
import requests
from DAO.usuarioDao import UsuarioDAO
from DAO.historialDao import HistorialDAO
from DTO.historialDto import HistorialDTO
from DTO.usuarioDto import UsuarioDTO

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    dao = UsuarioDAO()
    intentos = 0
    while intentos < 3:
        clear()
        print("=== LOGIN ECOTECH ===")
        username = input("Usuario: ")
        password = stdiomask.getpass(prompt="Contraseña: ", mask="*") # Ocultar password
        
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
            rol = input("Rol (admin/user): ")
            nuevo = UsuarioDTO(None, username, password, rol)
            if dao.crear(nuevo):
                print("Usuario creado exitosamente.")
            else:
                print("Error al crear usuario.")
            input("Enter...")

def obtener_indicador_api(indicador, fecha=None):
    base_url = "https://mindicador.cl/api"
    url = f"{base_url}/{indicador}"
    if fecha:
        url += f"/{fecha}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if fecha:
            if 'serie' in data and len(data['serie']) > 0:
                valor = data['serie'][0]['valor']
                fecha_valor = data['serie'][0]['fecha']
                return {'valor': valor, 'fecha': fecha_valor}
        else:
            if 'serie' in data and len(data['serie']) > 0:
                    valor = data['serie'][0]['valor']
                    fecha_valor = data['serie'][0]['fecha']
                    return {'valor': valor, 'fecha': fecha_valor}
        return None
    except Exception as e:
        print(f"Error al consultar API: {e}")
        return None

def menu_gestor_financiero(usuario_actual):
    historial_dao = HistorialDAO()
    
    while True:
        clear()
        print(f"=== GESTOR FINANCIERO (Usuario: {usuario_actual.username}) ===")
        print("1. Consultar Indicadores (UF, Dólar, Euro, etc.)")
        print("2. Ver Historial de Consultas")
        print("0. Volver")
        
        op = input("Opción: ")
        
        if op == "0": break
        elif op == "1":
            print("\nIndicadores disponibles: uf, ivp, dolar, euro, ipc, utm")
            indicador = input("Ingrese indicador a consultar: ").lower()
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
            input("Enter...")
            
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
