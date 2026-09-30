import re

# sub(): reemplaza todas las coincidencias del patrón por otro texto.
# por ejemplo, para ofuscar datos sensibles como el teléfono.
patron_telefono = r"[0-9]{10}"

texto = "El teléfono de Gael es 1123456789 y el de Oliver es 1198765432."

texto_ofuscado = re.sub(patron_telefono, "XXXXXXXXXX", texto)

print("Texto original:")
print(texto)
print("\nTexto después de ofuscar los teléfonos:")
print(texto_ofuscado)
