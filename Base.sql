CREATE TABLE persona(
	id serial NOT NULL PRIMARY KEY,
	nombre varchar(50),
	apellido varchar(50),
	tipo_documento varchar(20),
	num_documento varchar(20),
	celular varchar(30),
	ciudad varchar(40),
	direccion varchar(100)
	
);

CREATE TABLE usuario(
	id serial NOT NULL PRIMARY KEY,
	correo varchar(100),
	user varchar(20),
	password varchar(50),
	id_persona int NOT NULL,
	FOREIGN KEY(id_persona) REFERENCES persona(id)

	
);

CREATE TABLE doctor(
	id serial NOT NULL PRIMARY KEY,
	ident_med varchar(40),
	id_user int NOT NULL,
	FOREIGN KEY(id_user) REFERENCES usuario(id)
);

CREATE TABLE paciente(
	id serial NOT NULL PRIMARY KEY,
	id_user int NOT NULL,
	FOREIGN KEY(id_user) REFERENCES usuario(id)
	
);

CREATE TABLE admin(
	id serial NOT NULL PRIMARY KEY,
	id_user int NOT NULL,
	FOREIGN KEY(id_user) REFERENCES usuario(id)
);


CREATE TABLE consulta(
	id serial NOT NULL PRIMARY KEY,
	id_doctor int,
	id_paciente int,
	FOREIGN KEY(id_doctor) REFERENCES doctor(id),
	FOREIGN KEY(id_paciente) REFERENCES paciente(id),
	estado varchar(30)

	
);

CREATE TABLE llamada(
	id serial NOT NULL PRIMARY KEY,
	tipo varchar(20),
	duracion int,
	calificacion int,
	id_consulta int,
	FOREIGN KEY(id_consulta) REFERENCES consulta(id)
	
);

CREATE TABLE detalle_consulta(
	id serial NOT NULL PRIMARY KEY,
	fecha_reser date,
	fecha_prog date,
	precio decimal(10,2),
	calificacion int
	id_consulta int NOT NULL,
	FOREIGN KEY(id_consulta) REFERENCES consulta(id)
	
);

CREATE TABLE calificacion(
	id serial NOT NULL PRIMARY KEY,
	id_doctor int,
	id_paciente int,
	FOREIGN KEY(id_doctor) REFERENCES doctor(id),
	FOREIGN KEY(id_paciente) REFERENCES paciente(id),
	valor int
	
);

CREATE TABLE recetas(
	id serial NOT NULL PRIMARY KEY,
	id_consulta int,
	FOREIGN KEY(id_consulta) REFERENCES consulta(id),
	detalle varchar(500),
	
);

CREATE TABLE especialidad(
	id serial NOT NULL PRIMARY KEY,
	nombre varchar(100),
	descripcion varchar(300)
);


CREATE TABLE paquete(
	id serial NOT NULL PRIMARY KEY,
	descripcion varchar(300),
	precio decimal(10,2),
	duracion int,
	id_especialidad int,
	FOREIGN KEY(id_especialidad) REFERENCES especialidad(id)
	
);
