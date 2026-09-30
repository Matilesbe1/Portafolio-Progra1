import re

patron = r" [A-Za-z] [0-9] {3} "
codigo = "A123XYZ"

inicio = re.match(patron, codigo)
completo = re.fullmatch(patron, codigo)
'C) Utilizar re.search() para localizar la primera secuencia numérica dentro de una frase.'
frase = "Mi primer uso de expresiones recursivas en python en el 2026"
primera_secuencia_numerica = re.search(r"[0-9]+", frase) 
print(primera_secuencia_numerica.group())
'D) Mostrar group(), start(), end() y span() solamente cuando exista una coincidencia.'
match = re.match(patron, codigo)
if match:
    numeroEncontrado = match.group()
    posicionInicio = match.start()
    posicionFin = match.end()
    posicionSpan = match.span()

    print(f"Coincidencia encontrada: {numeroEncontrado}")
    print(f"Posición donde comienza: {posicionInicio}")
    print(f"Posición donde termina: {posicionFin}")
    print(f"Posición donde comienza y termina: {posicionSpan}")
else:
    print("No se encontró ninguna coincidencia.")
'E) Repetir una búsqueda con re.IGNORECASE.'
frase = "Mi primer uso de expresiones recursivas en python en el 2026"
primera_secuencia_numerica = re.search(r"mi", frase, re.IGNORECASE) 
print(primera_secuencia_numerica.group())