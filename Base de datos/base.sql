-- phpMyAdmin SQL Dump
-- version 5.2.3
-- Corregido para importación limpia
-- ==========================================

SET NAMES utf8mb4;

-- 1. DESACTIVAR VERIFICACIÓN DE LLAVES FORÁNEAS
-- Esto evita el error "Cannot delete or update a parent row" al crear las tablas
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;

-- 2. ASEGURAR QUE LA BASE DE DATOS EXISTA
CREATE DATABASE IF NOT EXISTS `base`;
USE `base`;

-- ==========================================
-- ESTRUCTURA DE TABLAS
-- ==========================================

-- Tabla: asignacion_empleados_proyectos
DROP TABLE IF EXISTS `asignacion_empleados_proyectos`;
CREATE TABLE IF NOT EXISTS `asignacion_empleados_proyectos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `empleado_id` int NOT NULL,
  `proyecto_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `empleado_id` (`empleado_id`),
  KEY `proyecto_id` (`proyecto_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: departamentos
DROP TABLE IF EXISTS `departamentos`;
CREATE TABLE IF NOT EXISTS `departamentos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `gerente` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: empleados
DROP TABLE IF EXISTS `empleados`;
CREATE TABLE IF NOT EXISTS `empleados` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `apellido` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `direccion` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `telefono` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `email` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `salario` decimal(10,2) DEFAULT NULL,
  `departamento_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `departamento_id` (`departamento_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: proyectos
DROP TABLE IF EXISTS `proyectos`;
CREATE TABLE IF NOT EXISTS `proyectos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` text COLLATE utf8mb4_unicode_ci,
  `fecha_inicio` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: registro_tiempo
DROP TABLE IF EXISTS `registro_tiempo`;
CREATE TABLE IF NOT EXISTS `registro_tiempo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `empleado_id` int NOT NULL,
  `proyecto_id` int NOT NULL,
  `fecha` date NOT NULL,
  `horas_trabajadas` decimal(5,2) DEFAULT NULL,
  `descripcion` text COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id`),
  KEY `empleado_id` (`empleado_id`),
  KEY `proyecto_id` (`proyecto_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ==========================================
-- VOLCADO DE DATOS (INSERTS)
-- ==========================================

INSERT INTO `departamentos` (`id`, `nombre`, `gerente`) VALUES
(1, 'Desarrollo de Software', 'Linus Torvalds'),
(2, 'Marketing Digital', 'Seth Godin'),
(3, 'Contabilidad y Finanzas', 'Warren Buffett'),
(4, 'Recursos Humanos', 'Oprah Winfrey'),
(5, 'Diseño Gráfico', 'Paula Scher');

INSERT INTO `empleados` (`id`, `nombre`, `apellido`, `direccion`, `telefono`, `email`, `fecha_inicio`, `salario`, `departamento_id`) VALUES
(10, 'Elon', 'Musk', 'Av. Apoquindo 5000, Las Condes', '+56 9 1234 5678', 'elon.musk@ecotech.com', '2024-06-01', 12500000.00, 1),
(11, 'Ada', 'Lovelace', 'Alameda 100, Santiago', '+56 9 9876 5432', 'ada.lovelace@ecotech.com', '2023-01-10', 3800000.00, 1),
(12, 'Don', 'Draper', 'Rosario Norte 400, Vitacura', '+56 9 5555 4444', 'don.draper@ecotech.com', '2024-03-15', 3000000.00, 2),
(13, 'Marie', 'Curie', 'Av. Providencia 2000, Providencia', '+56 2 2333 1212', 'marie.curie@ecotech.com', '2022-11-20', 4500000.00, 3),
(14, 'Beyoncé', 'Knowles', 'Costanera Sur 1, Renca', '+56 9 7777 0000', 'beyonce.k@ecotech.com', '2025-01-05', 2800000.00, 4),
(15, 'Banksy', 'Anonimo', 'Paseo Ahumada 300, Santiago', '+56 2 2444 8765', 'banksy.anonimo@ecotech.com', '2024-08-01', 3200000.00, 5);

INSERT INTO `proyectos` (`id`, `nombre`, `descripcion`, `fecha_inicio`) VALUES
(1, 'Sistema de Gestión de Talento (SGT)', 'Migración de la plataforma de RR.HH. a la nube.', '2025-01-15'),
(2, 'Campaña Viral "El Empleado Feliz"', 'Estrategia de marketing para atraer nuevos talentos.', '2025-03-01'),
(3, 'Aplicación Móvil de Control Horario', 'Desarrollo de una app para registrar el tiempo de trabajo.', '2025-05-20'),
(4, 'Auditoría Financiera Q3 2025', 'Revisión completa de las cuentas trimestrales de la empresa.', '2025-07-01');

INSERT INTO `asignacion_empleados_proyectos` (`id`, `empleado_id`, `proyecto_id`) VALUES
(13, 10, 3),
(14, 11, 1),
(15, 11, 3),
(16, 12, 2),
(17, 14, 1),
(18, 15, 2);

INSERT INTO `registro_tiempo` (`id`, `empleado_id`, `proyecto_id`, `fecha`, `horas_trabajadas`, `descripcion`) VALUES
(1, 10, 3, '2025-10-25', 8.00, 'Diseño de la arquitectura del backend.'),
(2, 11, 3, '2025-10-25', 7.50, 'Implementación de algoritmo de cifrado para login.'),
(3, 11, 1, '2025-10-26', 6.00, 'Revisión de requisitos y planificación de sprints.'),
(4, 12, 2, '2025-10-27', 4.00, 'Brainstorming de eslóganes y prueba A/B de colores.'),
(5, 14, 1, '2025-10-28', 8.50, 'Entrevistas con stakeholders para la fase de descubrimiento.'),
(6, 15, 2, '2025-10-29', 5.50, 'Creación de borradores de arte callejero para la campaña.');

-- ==========================================
-- APLICAR RELACIONES (FOREIGN KEYS)
-- ==========================================

ALTER TABLE `asignacion_empleados_proyectos`
  ADD CONSTRAINT `asignacion_empleados_proyectos_ibfk_1` FOREIGN KEY (`empleado_id`) REFERENCES `empleados` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `asignacion_empleados_proyectos_ibfk_2` FOREIGN KEY (`proyecto_id`) REFERENCES `proyectos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `empleados`
  ADD CONSTRAINT `empleados_ibfk_1` FOREIGN KEY (`departamento_id`) REFERENCES `departamentos` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE `registro_tiempo`
  ADD CONSTRAINT `registro_tiempo_ibfk_1` FOREIGN KEY (`empleado_id`) REFERENCES `empleados` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `registro_tiempo_ibfk_2` FOREIGN KEY (`proyecto_id`) REFERENCES `proyectos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

COMMIT;

-- 3. RESTAURAR CONFIGURACIÓN DE SEGURIDAD
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;