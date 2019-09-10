INSERT INTO medicina_persona(nombre,apellido,tipo_documento,numero_documento,fecha_nac,sexo,telefono,ciudad,direccion,imagen)
VALUES('Fanny','Valverde','cedula','0940384874','12/07/1998','F','0997363732','Guayaquil','Norte','https://via.placeholder.com/300x300'),
('Isabela','Vinces','cedula','0973893763','26/04/1997','F','0982637636','Guayaquil','Sur','https://via.placeholder.com/300x300'),
('Juan Jose','Flores','cedula','0932355232','06/06/1997','M','0973563553','Guayaquil','Este','https://via.placeholder.com/300x300'),
('Pedro','Mendoza','cedula','0988775231','15/05/1997','M','0983763689','Daule','Oeste','https://via.placeholder.com/300x300'),
('Roberto','Mena','cedula','0927363699','30/03/1997','M','0923473773','Cuenca','Centro','https://via.placeholder.com/300x300');


INSERT INTO medicina_usuario(email,username, password, persona_id_id)
VALUES('fmvalverde@gmail.com','fmvalverde','telemedicina123',1),
('ivinces@gmail.com','ivinces','telemedicina456',2),
('jjflores@gmail.com','jjflores','telemedicina789',3),
('pmendoza@gmail.com','pmendoza','telemedicina000',4),
('roberto@gmail.com','robertom','contrasena',5);

INSERT INTO medicina_especialidad(nombre,descripcion)
VALUES('Cardiologia','Especializacion en problemas del corazon y derivados'),
('Ginecologia','Especializacion en cuidado intimo femenino y tratamientos de embarazo '),
('Cirugia General','Especializacion en operaciones de tejidos musculares y organos');

INSERT INTO medicina_dias(nombre)
VALUES('Lunes'),
('Martes'),
('Miercoles'),
('Jueves'),
('Viernes'),
('Sabado'),
('Domingo');

INSERT INTO medicina_horario(hora_entrada,hora_salida,dias_id,doctor_id)
VALUES('10:30:00','15:30:00',1,2),
('12:30:00','18:30:00',4,1);

INSERT INTO medicina_doctor(identificador_medico, user_id_id,especialidad_id)
VALUES('0000000001',5,1),
('0000000002',2,3);

INSERT INTO medicina_administrador(user_id_id)
VALUES(1);

INSERT INTO medicina_paciente(user_id_id)
VALUES(3),
(4);

INSERT INTO medicina_examenes(nombre,descripcion)
VALUES('Examenes de orina','Determinar estados fisiológicos y bioquímicos'),
('Tomografia','Permite obtener imágenes radiológicas de una sección o un plano de un órgano.');


INSERT INTO medicina_consulta(estado,paciente_id_id,doctor_id_id)
VALUES('agendada',1,1),
('realizada',2,1),
('realizada',1,2);

INSERT INTO medicina_llamada(tipo,duracion,calificacion,consulta_id_id)
VALUES('videollamada',30,5,1),
('videollamada',45,4,3);

INSERT INTO medicina_detalle_consulta(fecha_reser,fecha_prog,precio,calificacion,consulta_id_id)
VALUES('2019-01-16','2019-09-05',100,0,1),
('2019-01-16','2019-09-02',50,5,2),
('2019-01-16','2019-09-03',75,4,3);


INSERT INTO medicina_paquete(nombre,descripcion,precio,duracion,especialidad_id)
VALUES('Chequeos y cuidados trimestrales','Controles de fertilidad y atencion general',200.00,12,2),
('Chequeos de presion arterial','Controles de presion y cuidados del corazon',200.00,12,1);

INSERT INTO medicina_tarifa(nombre,descripcion,precio)
VALUES('Basica','Doctores nuevos en el sistemas',8.00),
('Normal','Doctores con especialidad',10.00);