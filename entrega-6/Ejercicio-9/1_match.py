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
