import re

def busca_correo(texto):
  patron = r"[0-9a-zA-Z.+_-]+@[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+"
  resultado = re.finditer(patron,texto)
  return resultado

def muestra_correos(texto):
    correos = busca_correo(texto)
    contCorreos = 0
    for correo in correos:
        contCorreos += 1 
        print(f"Correo encontrado: {correo.group()}")
        print(f"Ubicacion: inicio = {correo.start()} fin = {correo.end()}")
    print("Se encontraron",contCorreos,"correos.")
    print("-"*10)

def busca_telefonos(texto):
    patron = r"[0-9]{4}-[0-9]{4}"
    resultado = re.findall(patron,texto)
    ubicacion = re.finditer(patron,texto)
    return resultado,ubicacion


def muestra_telefonos(texto):
    resultados,ubi = busca_telefonos(texto)
    if len(resultados)>0:
        print(f"Se encontraron {len(resultados)} teléfonos: ")
        for tel,match in zip(resultados,ubi):
            print(f"Tel: {tel} ubicado en {match.start()}-{match.end()}")
        print("-"*10)

def busca_codigos(texto):
    patron = r"[A-Z]{2}[0-9]{4}"
    resultado  = re.finditer(patron,texto)
    return resultado

def muestra_codigos(texto):
    resultados = busca_codigos(texto)
    print(f"Códigos encontrados: ")
    for match in resultados:
        print(f"{match.group()} | inicio = {match.start()} | fin = {match.end()}")

def main():
    datos = '''
    Hola, mi nombre es Juan Pérez y mi correo es [juan.perez@gmail.com]. También pueden contactarme en [juan123@empresa.com.ar].
    Mis teléfonos son 1234-5678 y 4567-8901. Mi código de cliente es AB1234 y el código de acceso es XY5678.
    Otros datos que no deberían coincidir:
        * Teléfono inválido: 12345678 
        * Teléfono inválido: 123-4567
        * Código inválido: ABC1234
        * Código inválido: AB123
        * Código inválido: ab1234
        * Email inválido: usuario@dominio
        * Email inválido: usuario@dominio.1
        * Número cualquiera: 987654321
        * Texto cualquiera: ABCDEFGH    
'''
    muestra_correos(datos)
    muestra_telefonos(datos)
    muestra_codigos(datos)
   
main()