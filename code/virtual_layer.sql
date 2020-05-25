SELECT c.*, listado.*
FROM ciudades as c
LEFT JOIN listado ON c.CODIGO_DANE = listado.codigo_dane
WHERE listado.nombre IS NOT NULL;
