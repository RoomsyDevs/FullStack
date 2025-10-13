

USE bdfullstack_insercion;


INSERT INTO usuarios (nombre, apellido, email, contrasena, telefono, rol, username)
VALUES ('Nicolás', 'Díaz', 'nico.diaz@example.com', 'pass123', '1167894321', 'turista', 'nicod');


-- Ver todos los hospedajes disponibles
SELECT h.titulo, h.precio_por_noche, u.nombre AS anfitrion, ub.ciudad, c.nombre AS categoria
FROM hospedajes h
JOIN usuarios u ON h.anfitrion_id = u.id
JOIN ubicaciones ub ON h.ubicacion_id = ub.id
JOIN categorias c ON h.categoria_id = c.id
WHERE h.disponible = 1;


UPDATE hospedajes
SET disponible = 0, estado = 'inactivo'
WHERE id = 3;

-- También podría cambiar el rol de un usuario
UPDATE usuarios
SET rol = 'anfitrion'
WHERE id = 4;


DELETE FROM usuarios
WHERE email = 'nico.diaz@example.com';

-- =======================
-- CONSULTA AVANZADA CON JOIN
-- =======================
SELECT u.nombre AS Anfitrion, h.titulo, ub.ciudad, c.nombre AS Categoria, h.estado
FROM hospedajes h
JOIN usuarios u ON h.anfitrion_id = u.id
JOIN ubicaciones ub ON h.ubicacion_id = ub.id
JOIN categorias c ON h.categoria_id = c.id
ORDER BY ub.provincia;
