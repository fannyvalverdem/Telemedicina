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