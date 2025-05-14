CREATE TABLE if not exists users(id_usuario INT PRIMARY KEY,
                   nombre VARCHAR(30),
                   documento_identidad VARCHAR(15),
                   fecha_nacimiento DATE(11),
                   correo VARCHAR(100)
                   );
                   