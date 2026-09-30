import re

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
