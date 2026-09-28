DROP DATABASE IF EXISTS esquema_seguidores;

CREATE DATABASE esquema_seguidores;

USE esquema_seguidores;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    email VARCHAR(45) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE seguidores (
    id INT AUTO_INCREMENT PRIMARY KEY,

    usuario_id INT NOT NULL,

    seguidor_id INT NOT NULL,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_seguidores_usuario
        FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id),

    CONSTRAINT fk_seguidores_seguidor
        FOREIGN KEY (seguidor_id)
        REFERENCES usuarios(id),

    CONSTRAINT uq_usuario_seguidor
        UNIQUE (usuario_id, seguidor_id)
);

INSERT INTO usuarios
(nombre, apellido, email)
VALUES
("Soraya", "Montenegro", "soraya@email.com"),
("Luis F.", "de la Vega", "luis@email.com"),
("Beatriz", "Pinzón", "beatriz@email.com"),
("Armando", "Mendoza", "armando@email.com"),
("Mia", "Colucci", "mia@email.com"),
("Roberto", "Pardo", "roberto@email.com");

INSERT INTO seguidores
(usuario_id, seguidor_id)
VALUES
(1, 2),
(1, 4),
(3, 2),
(5, 2),
(2, 3);

SELECT
    u.id AS usuario_id,
    CONCAT(u.nombre, " ", u.apellido) AS usuario_nombre,

    s.id AS seguidor_id,
    CONCAT(s.nombre, " ", s.apellido) AS seguidor_nombre

FROM seguidores f

INNER JOIN usuarios u
    ON f.usuario_id = u.id

INNER JOIN usuarios s
    ON f.seguidor_id = s.id

ORDER BY u.nombre, s.nombre;

SELECT * FROM usuarios;
SELECT * FROM seguidores;