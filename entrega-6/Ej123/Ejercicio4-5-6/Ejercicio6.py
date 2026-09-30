import re

'''a) Utilizar re.sub() para reemplazar todos los telefonos con formato 123-456-7890 por XXX-XXX-XXXX.'''
texto = "123-456-7890, 321-654-0987"
patron = r'[0-9]{3}-[0-9]{3}-[0-9]{4}'
nuevo_texto = re.sub(patron, "XXX-XXX-XXXX", texto)
print(nuevo_texto)

'''b) Utilizar re.split() para dividir un texto usando puntos, comas, signos de pregunta y espacios como separadores.'''
texto2 = "Hola, ¿como estas? Espero que bien. Yo estoy bien tambien."
patron2 = r'[.,? ]+'
split = re.split(patron2, texto2)
print(split)

'''c) Compilar un patrón mediante re.compile() y reutilizarlo con match(), findall() y sub().'''
patron_anio = re.compile(r"[0-9]{4}")
fechas = "07/08/2017|03/02/1984|17/03/2001"
anios = patron_anio.findall(fechas)
print(f"Findall(): {anios}")

resultado_match = patron_anio.match(fechas)
print(f"Match(): {resultado_match}")

resultado_sub = patron_anio.sub('XXXX', fechas)
print(f"Sub(): {resultado_sub}")

'''d) Explicar cuando mejora la legibilidad compilar una expresion regular.'''
'''Compilar con re.compile() mejora la legibilidad y el rendimiento cuando el mismo patrón se reutiliza varias veces, ya que se define una sola vez y Python no tiene que recompilarlo en cada llamada.'''