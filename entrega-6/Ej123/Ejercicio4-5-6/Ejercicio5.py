import re
texto = '''
Nombre: Lucas Abramo, Correo: labramo@uade.edu.ar, tel: 11-1234-5678, codigo: 123
Nombre: Gael Terrado, Correo: gterrado@uade.edu.ar, tel: 11-9876-5432, codigo: 456
Nombre: Lorenzo Rossi, Correo: lrossi@uade.edu.ar, tel: 11-1234-5679, codigo: 789
Nombre: Matias Lesbegueris, Correo: mlesbegueris@uade.edu.ar, tel: 11-9876-5431, codigo: 987
'''
'''a) Utilicen re.findall() para obtener todas las secuencias numericas.'''
patron = r'[0-9]+'
secuencias_numericas = re.findall(patron, texto)
print(secuencias_numericas)

'''b) Utilicen re.finditer() para recorrer todas las coincidencias e informar contenido, posicion inicial y final.'''
for match in re.finditer(patron, texto):
    print(f"Numero: {match.group()} - Inicio: {match.start()} - Final: {match.end()}")

'''c) Comparen el tipo de resultado que devuelve cada método.'''
print(type(re.findall(patron, texto)))    #  Me devuelve --> <class 'list'>
print(type(re.finditer(patron, texto)))   #  Me devuelve --> <class 'callable_iterator'>

'''d) Prueben un patron con grupos de captura y observen que findall() puede devolver tuplas en lugar de la coincidencia completa.'''
sin_grupos = re.findall('[0-9]{2}-[0-9]{4}-[0-9]{4}', texto)
print(sin_grupos)

con_grupos = re.findall('([0-9]{2})-([0-9]{4})-([0-9]{4})', texto)
print(con_grupos)  