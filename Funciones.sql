INSERT INTO persona(nombre,apellido,tipo_documento,num_documento,celular,ciudad,direccion)
VALUES('Fanny','Valverde','cedula','0940384874','0997363732','Guayaquil','Norte'),
('Isabela','Vinces,'cedula','0973893763','0982637636','Guayaquil','Sur'),
('Juan Jose','Flores','cedula','0932355232','0973563553','Guayaquil','Este'),
('Pedro','Mendoza','cedula','0988775231','0983763689','Daule','Oeste'),
('Roberto','Mena','cedula','0927363699','0923473773','Cuenca','Centro');


INSERT INTO usuario(email, username, password, id_persona)
VALUES('fmvalverde@gmail.com','fmvalverde','telemedicina123',1),
('ivinces@gmail.com','ivinces','telemedicina456',2),
('jjflores@gmail.com','jjflores','telemedicina789',3),
('pmendoza@gmail.com','pmendoza','telemedicina000',4);
('roberto@gmail.com','robertom','contrasena',5);

INSERT INTO doctor(identificador_medico, user_id)
VALUES(5);

INSERT INTO admin(user_id)
VALUES(1),
(2);

INSERT INTO paciente(user_id)
VALUES(3),
(4);


INSERT INTO consulta(estado,paciente_id,doctor_id)
VALUES('agendada',3,5),
('realizada',4,5),
('realizada',3,5);

INSERT INTO llamada(tipo,duracion,calificacion,consulta_id)
VALUES('videollamada',30,5,2),
('videollamada',45,4,3)

INSERT INTO detalle_consulta(fecha_reser,fecha_prog,precio,calificacion,consulta_id)
VALUES('2019-01-16','2019-09-05',100,0,1),
('2019-01-16','2019-09-02',50,5,2),
('2019-01-16','2019-09-03',75,4,3);
