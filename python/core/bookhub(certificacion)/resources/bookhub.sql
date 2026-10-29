-- CREACION DE LA BASE DE DATOS
CREATE DATABASE bookhub_bd;
USE bookhub_bd;

-- CREACION DE LA TABLA USUARIO
CREATE TABLE usuarios(
id_usuario INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(50) NOT NULL,
apellido VARCHAR(50) NOT NULL,
email VARCHAR(100) NOT NULL UNIQUE,
contrasena VARCHAR(50) NOT NULL,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- CREACION DE LA TABLA DE LIBROS
CREATE TABLE libros(
id_libro INT AUTO_INCREMENT PRIMARY KEY,
titulo VARCHAR(50) NOT NULL UNIQUE,
autor VARCHAR(50) NOT NULL,
genero VARCHAR(50) NOT NULL,
fecha_publicacion DATE NOT NULL,
descripcion TEXT NOT NULL,
usuario_id INT NOT NULL,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

CONSTRAINT fk_libro_usuario
	FOREIGN KEY (usuario_id)
	REFERENCES usuarios(id_usuario)
	ON DELETE CASCADE
	ON UPDATE CASCADE
);

-- CREACION DE LA TABLA DE FAVORITOS
CREATE TABLE favoritos (
    usuario_id INT NOT NULL,
    libro_id INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (usuario_id, libro_id),

    CONSTRAINT fk_favorito_usuario
        FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id_usuario)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT fk_favorito_libro
        FOREIGN KEY (libro_id)
        REFERENCES libros(id_libro)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

INSERT INTO usuarios (nombre, apellido, email, contrasena)
VALUES
('Ana', 'García', 'ana@bookhub.cl', 'TEMP_PASSWORD'),
('Carlos', 'Pérez', 'carlos@bookhub.cl', 'TEMP_PASSWORD'),
('Laura', 'Soto', 'laura@bookhub.cl', 'TEMP_PASSWORD'),
('Miguel', 'Rojas', 'miguel@bookhub.cl', 'TEMP_PASSWORD'),
('Sofía', 'Muñoz', 'sofia@bookhub.cl', 'TEMP_PASSWORD'),
('Daniel', 'Torres', 'daniel@bookhub.cl', 'TEMP_PASSWORD');

INSERT INTO libros
(titulo, autor, genero, fecha_publicacion, descripcion, usuario_id)
VALUES

(
    'Cien años de soledad',
    'Gabriel García Márquez',
    'Novela',
    '2024-05-10',
    'Una obra maestra del realismo mágico que narra la historia de la familia Buendía.',
    1
),

(
    'El principito',
    'Antoine de Saint-Exupéry',
    'Fábula',
    '2024-06-21',
    'Una historia sobre la amistad, el amor y la importancia de ver más allá de las apariencias.',
    1
),

(
    '1984',
    'George Orwell',
    'Ciencia Ficción',
    '2024-07-15',
    'Novela distópica sobre una sociedad controlada y vigilada constantemente.',
    1
),

(
    'Orgullo y prejuicio',
    'Jane Austen',
    'Romance',
    '2024-08-02',
    'Clásico de la literatura sobre relaciones, prejuicios y diferencias sociales.',
    1
),

(
    'Dune',
    'Frank Herbert',
    'Ciencia Ficción',
    '2024-04-12',
    'Una épica historia de política, poder y supervivencia en Arrakis.',
    2
),

(
    'Hábitos atómicos',
    'James Clear',
    'Desarrollo Personal',
    '2024-06-01',
    'Método práctico para mejorar hábitos pequeños y sostenibles.',
    3
),

(
    'El alquimista',
    'Paulo Coelho',
    'Novela',
    '2024-06-18',
    'Un joven pastor emprende un viaje para encontrar su tesoro y descubrir su propósito.',
    4
);

INSERT INTO favoritos (usuario_id, libro_id)
VALUES
(1, 5),
(1, 6),
(1, 7),
(2, 1),
(3, 1),
(3, 5),
(4, 2),
(5, 3),
(6, 4);

SELECT * FROM usuarios;
SELECT * FROM libros;
SELECT * FROM favoritos;

SELECT 
    u.nombre,
    u.apellido,
    l.titulo,
    l.autor,
    l.genero
FROM favoritos f
INNER JOIN usuarios u
    ON f.usuario_id = u.id_usuario
INNER JOIN libros l
    ON f.libro_id = l.id_libro
ORDER BY u.nombre;