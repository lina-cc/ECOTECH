import os
from DAO.departamentoDao import DepartamentoDAO
from DAO.empleadoDao import EmpleadoDAO
from DAO.proyectoDao import ProyectoDAO
from DAO.asignacionDao import AsignacionDAO
from DAO.registroTiempoDao import RegistroTiempoDAO
from DTO.departamentoDto import DepartamentoDTO
from DTO.empleadoDto import EmpleadoDTO
from DTO.proyectoDto import ProyectoDTO
from DTO.asignacionDto import AsignacionDTO
from DTO.registroTiempoDto import RegistroTiempoDTO

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# -------------------- SUBMENÚS --------------------

def menu_departamentos(dao):
    while True:
        clear()
        print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
        print("--- Gestión de Departamentos ---")
        print("1. Agregar departamento")
        print("2. Listar departamentos")
        print("3. Actualizar departamento")
        print("4. Eliminar departamento")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clear()
            print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
            nombre = input("Nombre del departamento: ")
            gerente = input("Gerente: ")
            nuevo = DepartamentoDTO(None, nombre, gerente)
            print("Departamento agregado." if dao.crear(nuevo) else "Error al agregar.")
            input("Enter para continuar...")
        elif opcion == "2":
            clear()
            print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
            for d in dao.listar():
                print(f"{d.id} | {d.nombre} | Gerente: {d.gerente}")
            input("Enter para continuar...")
        elif opcion == "3":
            clear()
            print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
            id = input("ID del departamento: ")
            datos = dao.buscar_por_id(id)
            if not datos:
                print("No encontrado.")
                input("Enter para continuar...")
                continue
            nombre = input(f"Nombre ({datos.nombre}): ") or datos.nombre
            gerente = input(f"Gerente ({datos.gerente}): ") or datos.gerente
            actualizado = DepartamentoDTO(id, nombre, gerente)
            print("Departamento actualizado." if dao.actualizar(actualizado) else "Error al actualizar.")
            input("Enter para continuar...")
        elif opcion == "4":
            clear()
            print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
            id = input("ID del departamento: ")
            print("Departamento eliminado." if dao.eliminar(id) else "Error al eliminar.")
            input("Enter para continuar...")
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
            input("Enter para continuar...")

def menu_empleados(dao):
    while True:
        clear()
        print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
        print("--- Gestión de Empleados ---")
        print("1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Actualizar empleado")
        print("4. Eliminar empleado")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clear()
            print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            fecha_inicio = input("Fecha Inicio (YYYY-MM-DD): ")
            salario = input("Salario: ")
            departamento_id = input("ID Departamento: ")
            nuevo = EmpleadoDTO(None, nombre, apellido, direccion, telefono, email, fecha_inicio, salario, departamento_id)
            print("Empleado agregado." if dao.crear(nuevo) else "Error al agregar.")
            input("Enter para continuar...")
        elif opcion == "2":
            clear()
            print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
            for e in dao.listar():
                print(f"{e.id} | {e.nombre} {e.apellido} | {e.email} | Dept ID: {e.departamento_id}")
            input("Enter para continuar...")
        elif opcion == "3":
            clear()
            print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
            id = input("ID del empleado: ")
            datos = dao.buscar_por_id(id)
            if not datos:
                print("No encontrado.")
                input("Enter para continuar...")
                continue
            nombre = input(f"Nombre ({datos.nombre}): ") or datos.nombre
            apellido = input(f"Apellido ({datos.apellido}): ") or datos.apellido
            direccion = input(f"Dirección ({datos.direccion}): ") or datos.direccion
            telefono = input(f"Teléfono ({datos.telefono}): ") or datos.telefono
            email = input(f"Email ({datos.email}): ") or datos.email
            fecha_inicio = input(f"Fecha Inicio ({datos.fecha_inicio}): ") or datos.fecha_inicio
            salario = input(f"Salario ({datos.salario}): ") or datos.salario
            departamento_id = input(f"ID Departamento ({datos.departamento_id}): ") or datos.departamento_id
            actualizado = EmpleadoDTO(id, nombre, apellido, direccion, telefono, email, fecha_inicio, salario, departamento_id)
            print("Empleado actualizado." if dao.actualizar(actualizado) else "Error al actualizar.")
            input("Enter para continuar...")
        elif opcion == "4":
            clear()
            print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
            id = input("ID del empleado: ")
            print("Empleado eliminado." if dao.eliminar(id) else "Error al eliminar.")
            input("Enter para continuar...")
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
            input("Enter para continuar...")

def menu_proyectos(dao):
    while True:
        clear()
        print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
        print("--- Gestión de Proyectos ---")
        print("1. Agregar proyecto")
        print("2. Listar proyectos")
        print("3. Actualizar proyecto")
        print("4. Eliminar proyecto")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clear()
            print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            fecha_inicio = input("Fecha Inicio (YYYY-MM-DD): ")
            nuevo = ProyectoDTO(None, nombre, descripcion, fecha_inicio)
            print("Proyecto agregado." if dao.crear(nuevo) else "Error al agregar.")
            input("Enter para continuar...")
        elif opcion == "2":
            clear()
            print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
            for p in dao.listar():
                print(f"{p.id} | {p.nombre} | {p.descripcion}")
            input("Enter para continuar...")
        elif opcion == "3":
            clear()
            id = input("ID del proyecto: ")
            datos = dao.buscar_por_id(id)
            if not datos:
                print("No encontrado.")
                input("Enter para continuar...")
                continue
            nombre = input(f"Nombre ({datos.nombre}): ") or datos.nombre
            descripcion = input(f"Descripción ({datos.descripcion}): ") or datos.descripcion
            fecha_inicio = input(f"Fecha Inicio ({datos.fecha_inicio}): ") or datos.fecha_inicio
            actualizado = ProyectoDTO(id, nombre, descripcion, fecha_inicio)
            print("Proyecto actualizado." if dao.actualizar(actualizado) else "Error al actualizar.")
            input("Enter para continuar...")
        elif opcion == "4":
            clear()
            print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
            id = input("ID del proyecto: ")
            print("Proyecto eliminado." if dao.eliminar(id) else "Error al eliminar.")
            input("Enter para continuar...")
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
            input("Enter para continuar...")

def menu_asignaciones(dao):
    while True:
        clear()
        print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
        print("--- Gestión de Asignaciones ---")
        print("1. Asignar empleado a proyecto")
        print("2. Listar asignaciones")
        print("3. Eliminar asignación")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clear()
            print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
            empleado_id = input("ID Empleado: ")
            proyecto_id = input("ID Proyecto: ")
            nuevo = AsignacionDTO(None, empleado_id, proyecto_id)
            print("Asignación agregada." if dao.crear(nuevo) else "Error al agregar.")
            input("Enter para continuar...")
        elif opcion == "2":
            clear()
            print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
            for a in dao.listar():
                print(f"ID: {a.id} | Empleado ID: {a.empleado_id} | Proyecto ID: {a.proyecto_id}")
            input("Enter para continuar...")
        elif opcion == "3":
            clear()
            print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
            id = input("ID de la asignación: ")
            print("Asignación eliminada." if dao.eliminar(id) else "Error al eliminar.")
            input("Enter para continuar...")
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
            input("Enter para continuar...")

def menu_registro_tiempo(dao):
    while True:
        clear()
        print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
        print("--- Registro de Tiempo ---")
        print("1. Registrar tiempo")
        print("2. Listar registros")
        print("3. Actualizar registro")
        print("4. Eliminar registro")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clear()
            print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
            empleado_id = input("ID Empleado: ")
            proyecto_id = input("ID Proyecto: ")
            fecha = input("Fecha (YYYY-MM-DD): ")
            horas = input("Horas trabajadas: ")
            descripcion = input("Descripción: ")
            nuevo = RegistroTiempoDTO(None, empleado_id, proyecto_id, fecha, horas, descripcion)
            print("Registro agregado." if dao.crear(nuevo) else "Error al agregar.")
            input("Enter para continuar...")
        elif opcion == "2":
            clear()
            print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
            for r in dao.listar():
                print(f"ID: {r.id} | Emp ID: {r.empleado_id} | Proy ID: {r.proyecto_id} | Horas: {r.horas_trabajadas}")
            input("Enter para continuar...")
        elif opcion == "3":
            clear()
            print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
            id = input("ID del registro: ")
            datos = dao.buscar_por_id(id)
            if not datos:
                print("No encontrado.")
                input("Enter para continuar...")
                continue
            empleado_id = input(f"ID Empleado ({datos.empleado_id}): ") or datos.empleado_id
            proyecto_id = input(f"ID Proyecto ({datos.proyecto_id}): ") or datos.proyecto_id
            fecha = input(f"Fecha ({datos.fecha}): ") or datos.fecha
            horas = input(f"Horas ({datos.horas_trabajadas}): ") or datos.horas_trabajadas
            descripcion = input(f"Descripción ({datos.descripcion}): ") or datos.descripcion
            actualizado = RegistroTiempoDTO(id, empleado_id, proyecto_id, fecha, horas, descripcion)
            print("Registro actualizado." if dao.actualizar(actualizado) else "Error al actualizar.")
            input("Enter para continuar...")
        elif opcion == "4":
            clear()
            print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
            id = input("ID del registro: ")
            print("Registro eliminado." if dao.eliminar(id) else "Error al eliminar.")
            input("Enter para continuar...")
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
            input("Enter para continuar...")

# MENÚ PRINCIPAL
def main():
    departamentoDAO = DepartamentoDAO()
    empleadoDAO = EmpleadoDAO()
    proyectoDAO = ProyectoDAO()
    asignacionDAO = AsignacionDAO()
    registroDAO = RegistroTiempoDAO()

    while True:
        clear()
        print("--- Sistema de Gestión de Empleados (ECOTECH) ---")
        print("--- Menú Principal ---")
        print("1. Departamentos")
        print("2. Empleados")
        print("3. Proyectos")
        print("4. Asignaciones")
        print("5. Registro de Tiempo")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_departamentos(departamentoDAO)
        elif opcion == "2":
            menu_empleados(empleadoDAO)
        elif opcion == "3":
            menu_proyectos(proyectoDAO)
        elif opcion == "4":
            menu_asignaciones(asignacionDAO)
        elif opcion == "5":
            menu_registro_tiempo(registroDAO)
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")
            input("Enter para continuar...")

if __name__ == "__main__":
    main()