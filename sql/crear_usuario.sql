CREATE TABLE if not exists users(id_usuario INT PRIMARY KEY,
                   nombres VARCHAR(30),
                   apellidos VARCHAR(30),
                   documento_identidad VARCHAR(15),
                   fecha_nacimiento DATE,
                   correo VARCHAR(100)
                   );
                   