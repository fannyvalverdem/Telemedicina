CREATE FUNCTION actualizar_calificacion()
RETURNS trigger AS $$
BEGIN

update medicina_doctor
set calificacion_total=(select AVG(valor)
from medicina_calificacion
WHERE doctor_id_id=NEW.doctor_id_id
GROUP BY doctor_id_id)
WHERE id=NEW.doctor_id_id;

RETURN NULL;
END; 
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER trigger_actualizar_calificacion
AFTER INSERT ON medicina_calificacion
FOR EACH ROW
EXECUTE PROCEDURE actualizar_calificacion();

CREATE FUNCTION actualizar_citas()
RETURNS trigger AS $$
BEGIN

update medicina_doctor
set citas_realizadas=(SELECT COUNT(*)
FROM medicina_consulta
WHERE estado='realizada' AND doctor_id_id=NEW.doctor_id_id
GROUP BY doctor_id_id)
WHERE id=NEW.doctor_id_id;

UPDATE medicina_doctor
set citas_realizadas=0
WHERE citas_realizadas IS NULL;

RETURN NULL;
END; 
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER trigger_actualizar_citas
AFTER INSERT OR UPDATE ON medicina_consulta
FOR EACH ROW
EXECUTE PROCEDURE actualizar_citas();


CREATE FUNCTION actualizar_citas_paciente()
RETURNS trigger AS $$
BEGIN

update medicina_paciente
set citas_realizadas=(SELECT COUNT(*)
FROM medicina_consulta
WHERE estado='realizada' AND paciente_id_id=NEW.paciente_id_id
GROUP BY paciente_id_id)
WHERE id=NEW.paciente_id_id;

UPDATE medicina_paciente
set citas_realizadas=0
WHERE citas_realizadas IS NULL;

RETURN NULL;
END; 
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER trigger_actualizar_citas_paciente
AFTER INSERT OR UPDATE ON medicina_consulta
FOR EACH ROW
EXECUTE PROCEDURE actualizar_citas_paciente();


CREATE FUNCTION actualizar_citas_especialidad()
RETURNS trigger AS $$
BEGIN

update medicina_detalles_especialidad
set citas_realizadas=(SELECT COUNT(*)
FROM medicina_consulta MC, medicina_detalle_consulta MDC
WHERE MC.id=MDC.consulta_id_id AND estado='realizada' AND especialidad_id=NEW.especialidad_id
GROUP BY especialidad_id)
WHERE especialidad_id=NEW.especialidad_id;

UPDATE medicina_detalles_especialidad
set citas_realizadas=0
WHERE citas_realizadas IS NULL;

RETURN NULL;
END; 
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER trigger_actualizar_citas_especialidad
AFTER INSERT OR UPDATE ON medicina_detalle_consulta
FOR EACH ROW
EXECUTE PROCEDURE actualizar_citas_especialidad();



CREATE FUNCTION actualizar_pagos_totales()
RETURNS trigger AS $$
BEGIN

update medicina_pagos_paciente
set pago_total=(SELECT SUM(precio)
FROM medicina_detalle_consulta DC, medicina_consulta MC 
Where DC.consulta_id_id=MC.id and MC.paciente_id_id=NEW.paciente_id_id
GROUP BY paciente_id_id)
WHERE paciente_id=NEW.paciente_id_id;

UPDATE medicina_pagos_paciente
set pago_total=0
WHERE pago_total IS NULL;

RETURN NULL;
END; 
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER trigger_actualizar_pagos_totales
AFTER INSERT OR UPDATE ON medicina_consulta
FOR EACH ROW
EXECUTE PROCEDURE actualizar_pagos_totales();


CREATE FUNCTION actualizar_paciente_pagos()
RETURNS trigger AS $$
BEGIN

INSERT INTO medicina_pagos_paciente(pago_total,paciente_id)
VALUES (0,NEW.id);

RETURN NULL;
END; 
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER trigger_actualizar_paciente_pagos
AFTER INSERT ON medicina_paciente
FOR EACH ROW
EXECUTE PROCEDURE actualizar_paciente_pagos();


CREATE FUNCTION actualizar_pagos_especialidad()
RETURNS trigger AS $$
BEGIN

update medicina_detalles_especialidad
set pagos_total=(SELECT SUM(precio)
FROM medicina_detalle_consulta MDC,medicina_consulta MC
Where MC.id=MDC.consulta_id_id AND estado='realizada' AND especialidad_id=NEW.especialidad_id
GROUP BY especialidad_id)
WHERE especialidad_id=NEW.especialidad_id;

UPDATE medicina_detalles_especialidad
set pagos_total=0
WHERE pagos_total IS NULL;

RETURN NULL;
END; 
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER trigger_actualizar_pagos_especialidad
AFTER INSERT ON medicina_detalle_consulta
FOR EACH ROW
EXECUTE PROCEDURE actualizar_pagos_especialidad();

CREATE FUNCTION actualizar_total_doc_especialidad()
RETURNS trigger AS $$
BEGIN

update medicina_detalles_especialidad
set total_doctor=(SELECT COUNT(*)
FROM medicina_matchespecialidades
WHERE especialidad_id=NEW.especialidad_id
GROUP BY especialidad_id)
WHERE especialidad_id=NEW.especialidad_id;

UPDATE medicina_detalles_especialidad
set total_doctor=0
WHERE total_doctor IS NULL;

RETURN NULL;
END; 
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER trigger_actualizar_doc_especialidad
AFTER INSERT OR UPDATE ON medicina_matchespecialidades
FOR EACH ROW
EXECUTE PROCEDURE actualizar_total_doc_especialidad();

CREATE FUNCTION actualizar_detalles_especialidad()
RETURNS trigger AS $$
BEGIN

INSERT INTO medicina_detalles_especialidad(pagos_total,total_doctor,citas_realizadas,especialidad_id)
VALUES (0,0,0,NEW.id);

RETURN NULL;
END; 
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER trigger_actualizar_detalles_especialidad
AFTER INSERT ON medicina_especialidad
FOR EACH ROW
EXECUTE PROCEDURE actualizar_detalles_especialidad();


CREATE FUNCTION actualizar_detalles_paquetes()
RETURNS trigger AS $$
BEGIN

INSERT INTO medicina_detalles_paquetes(pagos_total,total_pacientes,paquetes_id)
VALUES (0,0,NEW.id);

RETURN NULL;
END; 
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER trigger_actualizar_detalles_paquetes
AFTER INSERT ON medicina_paquete
FOR EACH ROW
EXECUTE PROCEDURE actualizar_detalles_paquetes();


CREATE FUNCTION actualizar_total_pacientes_paquete()
RETURNS trigger AS $$
BEGIN

update medicina_detalles_paquetes
set total_pacientes=(SELECT COUNT(*)
FROM medicina_matchpaquetes
WHERE paquete_id=NEW.paquete_id
GROUP BY paquete_id)
WHERE paquete_id=NEW.paquete_id;

UPDATE medicina_detalles_paquetes
set total_pacientes=0
WHERE total_pacientes IS NULL;

RETURN NULL;
END; 
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER trigger_actualizar_total_pacientes_paquete
AFTER INSERT OR UPDATE ON medicina_matchpaquetes
FOR EACH ROW
EXECUTE PROCEDURE actualizar_total_pacientes_paquete();


DROP TRIGGER 