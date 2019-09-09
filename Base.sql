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

CREATE TABLE detalle_consulta(
	id serial NOT NULL PRIMARY KEY,
	fecha date,
	precio int,
	calificacion int
	
);

CREATE TABLE llamada(
	id serial NOT NULL PRIMARY KEY,
	tipo varchar(20),
	duracion int,
	calificacion int
	
);

CREATE TABLE consulta(
	id serial NOT NULL PRIMARY KEY,
	id_doctor int,
	id_paciente int,
	id_detalle int,
	llamada int,
	FOREIGN KEY(id_doctor) REFERENCES doctor(id),
	FOREIGN KEY(id_paciente) REFERENCES paciente(id),
	FOREIGN KEY(id_detalle) REFERENCES detalle_consulta(id),
	FOREIGN KEY(id_llamada) REFERENCES llamada(id),
	estado varchar(30)

	
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

