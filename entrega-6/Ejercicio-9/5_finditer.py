import re

# finditer(): igual que findall(), pero devuelve un iterador de objetos
# Match (con posición, no solo el texto encontrado).
patron_comision = r"[A-Z]{3}-[0-9]{3}"

texto = "Las comisiones inscriptas son ABC-123, XYZ-456 y KLM-789 para este cuatrimestre."

for match in re.finditer(patron_comision, texto):
    print(f"Comisión: {match.group()} | inicio={match.start()}, fin={match.end()}")
