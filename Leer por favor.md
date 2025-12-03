Proyecto POO Parte 1: Sistema de Gestión de Empleados

Esta parte se centra en la gestión administrativa interna de la empresa.



Objetivo: Administrar la estructura organizativa y operativa.



Módulos Principales:

* Departamentos: Gestión de áreas de la empresa (Crear, Listar, Actualizar, Eliminar).
* Empleados: Gestión del personal, incluyendo datos personales, salario y asignación a departamentos.
* Proyectos: Administración de los proyectos de la empresa.
* Asignaciones: Vinculación de empleados a proyectos específicos.
* Registro de Tiempo: Control de horas trabajadas por empleado en cada proyecto.
* Arquitectura: Utiliza el patrón DAO (Data Access Object) para la persistencia de datos y DTO (Data Transfer Object) para la transferencia de información.



Proyecto POO Parte 2: Gestión de Usuarios y Financiera

Esta parte añade capas de seguridad y herramientas financieras externas.



Objetivo: Controlar el acceso al sistema y proveer herramientas de consulta económica.



Módulos Principales:

* Autenticación (Login): Sistema de inicio de sesión con roles (admin/user).
* Gestión de Usuarios (Solo Admin): Administración de cuentas de acceso al sistema.
* Gestor Financiero:
* Consulta de Indicadores: Conexión a la API mindicador.cl para obtener valores en tiempo real o históricos de indicadores económicos (UF, Dólar, Euro, etc.).
* Historial de Consultas: Registro de todas las consultas realizadas por los usuarios.
* Tecnología Destacada: Integración con API REST externa usando la librería request y manejo de fechas con datetime.
* Creación de un super admin. Usuario: admin contraseña: admin123



