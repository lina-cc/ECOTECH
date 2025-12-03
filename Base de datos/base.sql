-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 03-12-2025 a las 21:46:29
-- Versión del servidor: 8.4.7
-- Versión de PHP: 8.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `base`
--
CREATE DATABASE IF NOT EXISTS `base` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `base`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asignacion_empleados_proyectos`
--

DROP TABLE IF EXISTS `asignacion_empleados_proyectos`;
CREATE TABLE IF NOT EXISTS `asignacion_empleados_proyectos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `empleado_id` int NOT NULL,
  `proyecto_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `empleado_id` (`empleado_id`),
  KEY `proyecto_id` (`proyecto_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `asignacion_empleados_proyectos`
--

INSERT INTO `asignacion_empleados_proyectos` (`id`, `empleado_id`, `proyecto_id`) VALUES
(13, 10, 3),
(14, 11, 1),
(15, 11, 3),
(16, 12, 2),
(17, 14, 1),
(18, 15, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamentos`
--

DROP TABLE IF EXISTS `departamentos`;
CREATE TABLE IF NOT EXISTS `departamentos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `gerente` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `departamentos`
--

INSERT INTO `departamentos` (`id`, `nombre`, `gerente`) VALUES
(1, 'Desarrollo de Software', 'Linus Torvalds'),
(2, 'Marketing Digital', 'Seth Godin'),
(3, 'Contabilidad y Finanzas', 'Warren Buffett'),
(4, 'Recursos Humanos', 'Oprah Winfrey'),
(5, 'Diseño Gráfico', 'Paula Scher');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

DROP TABLE IF EXISTS `empleados`;
CREATE TABLE IF NOT EXISTS `empleados` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `apellido` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `direccion` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `telefono` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `salario` decimal(10,2) DEFAULT NULL,
  `departamento_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `departamento_id` (`departamento_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`id`, `nombre`, `apellido`, `direccion`, `telefono`, `email`, `fecha_inicio`, `salario`, `departamento_id`) VALUES
(10, 'Elon', 'Musk', 'Av. Apoquindo 5000, Las Condes', '+56 9 1234 5678', 'elon.musk@ecotech.com', '2024-06-01', 12500000.00, 1),
(11, 'Ada', 'Lovelace', 'Alameda 100, Santiago', '+56 9 9876 5432', 'ada.lovelace@ecotech.com', '2023-01-10', 3800000.00, 1),
(12, 'Don', 'Draper', 'Rosario Norte 400, Vitacura', '+56 9 5555 4444', 'don.draper@ecotech.com', '2024-03-15', 3000000.00, 2),
(13, 'Marie', 'Curie', 'Av. Providencia 2000, Providencia', '+56 2 2333 1212', 'marie.curie@ecotech.com', '2022-11-20', 4500000.00, 3),
(14, 'Beyoncé', 'Knowles', 'Costanera Sur 1, Renca', '+56 9 7777 0000', 'beyonce.k@ecotech.com', '2025-01-05', 2800000.00, 4),
(15, 'Banksy', 'Anonimo', 'Paseo Ahumada 300, Santiago', '+56 2 2444 8765', 'banksy.anonimo@ecotech.com', '2024-08-01', 3200000.00, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial_consultas`
--

DROP TABLE IF EXISTS `historial_consultas`;
CREATE TABLE IF NOT EXISTS `historial_consultas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `indicador` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `valor` decimal(10,2) NOT NULL,
  `fecha_valor` date NOT NULL,
  `fecha_consulta` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `origen` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `usuario_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usuario_id` (`usuario_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `historial_consultas`
--

INSERT INTO `historial_consultas` (`id`, `indicador`, `valor`, `fecha_valor`, `fecha_consulta`, `origen`, `usuario_id`) VALUES
(1, 'utm', 69542.00, '2025-11-01', '2025-11-29 18:22:52', 'mindicador.cl', 2),
(4, 'uf', 39643.59, '2025-12-02', '2025-12-02 20:28:05', 'mindicador.cl', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyectos`
--

DROP TABLE IF EXISTS `proyectos`;
CREATE TABLE IF NOT EXISTS `proyectos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `fecha_inicio` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `proyectos`
--

INSERT INTO `proyectos` (`id`, `nombre`, `descripcion`, `fecha_inicio`) VALUES
(1, 'Sistema de Gestión de Talento (SGT)', 'Migración de la plataforma de RR.HH. a la nube.', '2025-01-15'),
(2, 'Campaña Viral \"El Empleado Feliz\"', 'Estrategia de marketing para atraer nuevos talentos.', '2025-03-01'),
(3, 'Aplicación Móvil de Control Horario', 'Desarrollo de una app para registrar el tiempo de trabajo.', '2025-05-20'),
(4, 'Auditoría Financiera Q3 2025', 'Revisión completa de las cuentas trimestrales de la empresa.', '2025-07-01');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_tiempo`
--

DROP TABLE IF EXISTS `registro_tiempo`;
CREATE TABLE IF NOT EXISTS `registro_tiempo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `empleado_id` int NOT NULL,
  `proyecto_id` int NOT NULL,
  `fecha` date NOT NULL,
  `horas_trabajadas` decimal(5,2) DEFAULT NULL,
  `descripcion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id`),
  KEY `empleado_id` (`empleado_id`),
  KEY `proyecto_id` (`proyecto_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `registro_tiempo`
--

INSERT INTO `registro_tiempo` (`id`, `empleado_id`, `proyecto_id`, `fecha`, `horas_trabajadas`, `descripcion`) VALUES
(1, 10, 3, '2025-10-25', 8.00, 'Diseño de la arquitectura del backend.'),
(2, 11, 3, '2025-10-25', 7.50, 'Implementación de algoritmo de cifrado para login.'),
(3, 11, 1, '2025-10-26', 6.00, 'Revisión de requisitos y planificación de sprints.'),
(4, 12, 2, '2025-10-27', 4.00, 'Brainstorming de eslóganes y prueba A/B de colores.'),
(5, 14, 1, '2025-10-28', 8.50, 'Entrevistas con stakeholders para la fase de descubrimiento.'),
(6, 15, 2, '2025-10-29', 5.50, 'Creación de borradores de arte callejero para la campaña.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `password_hash` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `rol` enum('admin','user') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'user',
  `empleado_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `empleado_id` (`empleado_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `username`, `password_hash`, `rol`, `empleado_id`) VALUES
(2, 'admin', '$2b$12$ZD98nw8Qan3j/GjBClUO.umD6bc61B1Z0/sAicVzq/lZ1/DmOZB4q', 'admin', NULL),
(7, 'ccarisg', '$2b$12$KVDH0mHvnI3t3EYLF9P0MeNH0SalYgN7xgOgL36ICJKjtXQ3nn3om', 'admin', NULL);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD CONSTRAINT `empleados_ibfk_1` FOREIGN KEY (`departamento_id`) REFERENCES `departamentos` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Filtros para la tabla `historial_consultas`
--
ALTER TABLE `historial_consultas`
  ADD CONSTRAINT `historial_consultas_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `registro_tiempo`
--
ALTER TABLE `registro_tiempo`
  ADD CONSTRAINT `registro_tiempo_ibfk_1` FOREIGN KEY (`empleado_id`) REFERENCES `empleados` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `registro_tiempo_ibfk_2` FOREIGN KEY (`proyecto_id`) REFERENCES `proyectos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`empleado_id`) REFERENCES `empleados` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
