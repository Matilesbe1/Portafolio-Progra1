import re

# fullmatch(): exige que la cadena completa coincida con el patrón,
# de principio a fin, sin nada sobrante.
patron_comision = r"[A-Z]{3}-[0-9]{3}"

cadenas = ["ABC-123", "ABC-1234", "XABC-123", "ABC-123extra"]

for cadena in cadenas:
    resultado = re.fullmatch(patron_comision, cadena)
    if resultado:
        print(f'fullmatch("{cadena}") VÁLIDO')
    else:
        print(f'fullmatch("{cadena}") INVÁLIDO (no coincide toda la cadena)')
