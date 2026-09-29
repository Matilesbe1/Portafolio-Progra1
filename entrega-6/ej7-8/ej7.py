import re

def retorno_booleano(patron,elemento):
 if re.fullmatch(patron,elemento) is not None:
  return True
 else: 
  return False

def validar_legajo(legajo):
 patron = r"[0-9]{5}"
 return retorno_booleano(patron,legajo)

def validar_codigo(codigo):
 patron = r"[A-Z]{2}[0-9]{4}"
 return retorno_booleano(patron,codigo)

def validar_telefono(telefono):
 patron = r"[0-9]{4}-[0-9]{4}"
 return retorno_booleano(patron,telefono)

def validar_correo(correo):
  patron = r"[0-9a-zA-Z.+_-]+@[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+"
  return retorno_booleano(patron,correo)

def validar_importe(importe):
 patron = r"\$[0-9]+"
 return retorno_booleano(patron,importe)

def validar_patente(patente):
 patron = r"[A-Z]{2}[0-9]{3}[A-Z]{2}"
 return retorno_booleano(patron,patente)

def pruebas(nombre,funcion,valido,invalido):

  print(f"{'-'*5} {nombre} {'-'*5}")

  print("# Pruebas Válidas")
  for x in valido:
    print(x,"|",funcion(x))

  print("# Pruebas Inválidas")
  for z in invalido:
    print(z,"|",funcion(z))

  print("# Cadena Vacía")
  print('\"\"',"|",funcion(""))

  print()

 

def main():
    pruebas("LEGAJOS",validar_legajo,["12345","11111","17283"],["aAa-5","123","-12345"])
    pruebas("CÓDIGOS",validar_codigo,["AB1234","BC5678","DF9101"],["AAAAA","a12345","1242345"])
    pruebas("TELÉFONOS",validar_telefono,["1234-5678","1111-2222","4432-7474"],["unod-ostr","12345678","123-45678"])
    pruebas("CORREOS",validar_correo,["lrossi@uade.edu.ar","mlesbegueris06@yahoo.com.ar","enner-valencia@3pepas.com"],["pedro@com","lrossi.uade.edu.ar","lrossi@uade."])
    pruebas("IMPORTE",validar_importe,["$123","$100000","$00"],["mil quinientos","1.5","USD 110","123"])
    pruebas("PATENTE",validar_patente,["AI400AV","AH999CD","AA000ZZ"],["ENR342","233ABC","ai567ef"])
main()