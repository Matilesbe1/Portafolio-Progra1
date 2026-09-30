import re

# findall(): devuelve todas las coincidencias del patrón en la cadena,
# como una lista.
patron_comision = r"[A-Z]{3}-[0-9]{3}"

texto = "Las comisiones inscriptas son ABC-123, XYZ-456 y KLM-789 para este cuatrimestre."

comisiones = re.findall(patron_comision, texto)

print(f"Comisiones encontradas: {comisiones}")
print(f"Cantidad total: {len(comisiones)}")
