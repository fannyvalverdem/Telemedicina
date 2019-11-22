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
$$ LANGUAGE 'plpgsql'

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
$$ LANGUAGE 'plpgsql'

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
$$ LANGUAGE 'plpgsql'

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
$$ LANGUAGE 'plpgsql'

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
$$ LANGUAGE 'plpgsql'

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
$$ LANGUAGE 'plpgsql'

CREATE TRIGGER trigger_actualizar_paciente_pagos
AFTER INSERT ON medicina_paciente
FOR EACH ROW
EXECUTE PROCEDURE actualizar_paciente_pagos();


CREATE FUNCTION actualizar_pagos_especialidad()
RETURNS trigger AS $$
BEGIN

update medicina_detalles_especialidad
set pagos_total=(SELECT SUM(precio)
FROM medicina_detalle_consulta
Where especialidad_id=NEW.especialidad_id
GROUP BY especialidad_id)
WHERE especialidad_id=NEW.especialidad_id;

UPDATE medicina_detalles_especialidad
set pagos_total=0
WHERE pagos_total IS NULL;

RETURN NULL;
END; 
$$ LANGUAGE 'plpgsql'

CREATE TRIGGER trigger_actualizar_pagos_especialidad
AFTER INSERT ON medicina_detalle_consulta
FOR EACH ROW
EXECUTE PROCEDURE actualizar_pagos_especialidad();




DROP trigger trigger_actualizar_citas_especialidad On medicina_detalle_consulta;

DROP FUNCTION actualizar_citas_especialidad()
