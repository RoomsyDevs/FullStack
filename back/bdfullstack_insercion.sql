-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 12-10-2025 a las 20:58:54
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bdfullstack_insercion`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categorias`
--

CREATE TABLE `categorias` (
  `id` int(11) NOT NULL,
  `nombre` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categorias`
--

INSERT INTO `categorias` (`id`, `nombre`) VALUES
(3, 'Cabaña'),
(1, 'Casa'),
(2, 'Departamento'),
(5, 'Habitación privada'),
(4, 'Hostel');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `hospedajes`
--

CREATE TABLE `hospedajes` (
  `id` int(11) NOT NULL,
  `anfitrion_id` int(11) NOT NULL,
  `titulo` varchar(120) NOT NULL,
  `descripcion` text NOT NULL,
  `precio_por_noche` decimal(10,2) NOT NULL,
  `capacidad` int(11) NOT NULL,
  `direccion` varchar(160) NOT NULL DEFAULT 'No contemplado en este sprint',
  `ubicacion_id` int(11) NOT NULL,
  `categoria_id` int(11) NOT NULL,
  `disponible` tinyint(1) NOT NULL DEFAULT 1,
  `estado` varchar(20) NOT NULL DEFAULT 'activo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `hospedajes`
--

INSERT INTO `hospedajes` (`id`, `anfitrion_id`, `titulo`, `descripcion`, `precio_por_noche`, `capacidad`, `direccion`, `ubicacion_id`, `categoria_id`, `disponible`, `estado`) VALUES
(1, 1, 'Casa céntrica con patio', 'Alojamiento amplio cerca del centro de Córdoba', 18000.00, 4, 'Av. Colón 345', 1, 1, 1, 'activo'),
(2, 2, 'Departamento moderno en Mendoza', 'Ideal para parejas, con vista a la montaña', 22000.00, 2, 'San Martín 880', 2, 2, 1, 'activo'),
(3, 1, 'Cabaña en las sierras', 'Perfecta para desconectarse, rodeada de naturaleza', 25000.00, 5, 'Camino al Dique 234', 1, 3, 1, 'activo'),
(4, 5, 'Hostel en Bariloche', 'Camas compartidas con cocina comunitaria', 12000.00, 8, 'Mitre 1024', 4, 4, 1, 'activo'),
(5, 2, 'Habitación privada en Mar del Plata', 'A pasos de la playa, incluye desayuno', 15000.00, 2, 'Av. Colón 2200', 3, 5, 1, 'activo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ubicaciones`
--

CREATE TABLE `ubicaciones` (
  `id` int(11) NOT NULL,
  `ciudad` varchar(80) NOT NULL,
  `provincia` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ubicaciones`
--

INSERT INTO `ubicaciones` (`id`, `ciudad`, `provincia`) VALUES
(1, 'Córdoba', 'Córdoba'),
(2, 'Mendoza', 'Mendoza'),
(3, 'Mar del Plata', 'Buenos Aires'),
(4, 'Bariloche', 'Río Negro'),
(5, 'Salta', 'Salta');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `apellido` varchar(60) NOT NULL,
  `email` varchar(120) NOT NULL,
  `contrasena` varchar(255) NOT NULL,
  `telefono` varchar(30) DEFAULT NULL,
  `fecha_alta` datetime DEFAULT current_timestamp(),
  `rol` varchar(20) NOT NULL,
  `activo` tinyint(1) NOT NULL DEFAULT 1,
  `username` varchar(50) DEFAULT NULL,
  `estado` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `apellido`, `email`, `contrasena`, `telefono`, `fecha_alta`, `rol`, `activo`, `username`, `estado`) VALUES
(1, 'Florencia', 'Pérez', 'laura.perez@example.com', '1234', '3516547890', '2025-10-12 15:58:43', 'anfitrion', 1, 'laurap', 1),
(2, 'Agustina', 'Gómez', 'martin.gomez@example.com', 'abcd', '2617894561', '2025-10-12 15:58:43', 'anfitrion', 1, 'marting', 1),
(3, 'Sofía', 'Ramírez', 'sofia.ramirez@example.com', 'qwerty', '2234567890', '2025-10-12 15:58:43', 'turista', 1, 'sofiar', 1),
(4, 'Ignacio', 'Fernández', 'julian.fernandez@example.com', 'zxcvb', '2944123456', '2025-10-12 15:58:43', 'turista', 1, 'julianf', 1),
(5, 'Griselda', 'López', 'paula.lopez@example.com', 'asdf', '3876543210', '2025-10-12 15:58:43', 'anfitrion', 1, 'paulal', 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `hospedajes`
--
ALTER TABLE `hospedajes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `anfitrion_id` (`anfitrion_id`),
  ADD KEY `ubicacion_id` (`ubicacion_id`),
  ADD KEY `categoria_id` (`categoria_id`);

--
-- Indices de la tabla `ubicaciones`
--
ALTER TABLE `ubicaciones`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categorias`
--
ALTER TABLE `categorias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `hospedajes`
--
ALTER TABLE `hospedajes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `ubicaciones`
--
ALTER TABLE `ubicaciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `hospedajes`
--
ALTER TABLE `hospedajes`
  ADD CONSTRAINT `hospedajes_ibfk_1` FOREIGN KEY (`anfitrion_id`) REFERENCES `usuarios` (`id`),
  ADD CONSTRAINT `hospedajes_ibfk_2` FOREIGN KEY (`ubicacion_id`) REFERENCES `ubicaciones` (`id`),
  ADD CONSTRAINT `hospedajes_ibfk_3` FOREIGN KEY (`categoria_id`) REFERENCES `categorias` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
