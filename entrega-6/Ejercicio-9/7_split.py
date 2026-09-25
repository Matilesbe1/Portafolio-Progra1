import re

# split(): divide la cadena usando el patrón como delimitador.
# Acá dividimos un listado de comisiones separadas por coma, punto y/o espacios.
texto = "ABC-123, XYZ-456,KLM-789.  DEF-321"

patron_separador = r"[,.\s]+"

partes = re.split(patron_separador, texto)

print("Partes obtenidas al dividir:")
for parte in partes:
    print(f"- {parte}")
