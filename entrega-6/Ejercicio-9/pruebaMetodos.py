import re

# match(): busca coincidencia solo al inicio de la cadena.
# Puede "sobrar" texto después y aun así matchea.
patron_legajo = r"[0-9]+"

cadenas = ["1243432", "1243432abc", "abc1243432"]

for cadena in cadenas:
    resultado = re.match(patron_legajo, cadena)
    if resultado:
        print(f'match("{cadena}") coincide: "{resultado.group()}" (pero la cadena entera es "{cadena}")')
    else:
        print(f'match("{cadena}") no coincide')


# search(): busca la coincidencia en cualquier posición de la cadena,
# no solo al principio. Devuelve la primera que encuentra.
patron_telefono = r"[0-9]{10}"

texto = "El teléfono de Gael es 1123456789, contactalo por ahí."

resultado = re.search(patron_telefono, texto)

if resultado:
    print(f"Se encontró un número: {resultado.group()}")
    print(f"Posición: inicio={resultado.start()}, fin={resultado.end()}")
else:
    print("No se encontró ningún número de teléfono en el texto.")


# fullmatch(): exige que la cadena completa coincida con el patrón,
# de principio a fin, sin nada sobrante.
patron_comision = r"[A-Z]{3}-[0-9]{3}"

cadenas = ["ABC-123", "ABC-1234", "XABC-123", "ABC-123extra"]

for cadena in cadenas:
    resultado = re.fullmatch(patron_comision, cadena)
    if resultado:
        print(f'fullmatch("{cadena}")  VÁLIDO')
    else:
        print(f'fullmatch("{cadena}") INVÁLIDO (no coincide toda la cadena)')


# finditer(): igual que findall(), pero devuelve un iterador de objetos
# Match (con posición, no solo el texto encontrado).
patron_comision = r"[A-Z]{3}-[0-9]{3}"

texto = "Las comisiones inscriptas son ABC-123, XYZ-456 y KLM-789 para este cuatrimestre."

for match in re.finditer(patron_comision, texto):
    print(f"Comisión: {match.group()} | inicio={match.start()}, fin={match.end()}")

