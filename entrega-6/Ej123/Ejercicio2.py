import re
def posicionInicioYFin():
    texto='Mi nombre es Matias. Mis cuentas de banco estan en: $100.000 pesos '
    condicion=r'^M.'
    condicion2=r'os.$'
    palabras= re.findall(condicion, texto)
    palabras2=re.findall(condicion2, texto)

    for palabra in palabras:
        print(palabra)
    for palabra2 in palabras2:
        print(palabra2)

def cualquierCaracter():
    texto='Mi nombre es Matias. Mis cuentas de banco estan en: $100.000 pesos'
    condicion=r'[a-z]e.'
    palabras=re.findall(condicion, texto)
    for palabra in palabras:
        print(palabra)

def claseCaracteres():
    texto='ABCDEF123'
    condicion=r'[A-Z]{3}[0-9]{3}'
    caracteres=re.findall(condicion, texto)
    for caracter in caracteres:
        print(caracter)

def negacionComienzo():
    texto='Realizo'
    condicion=r'[^R.]'
    match=re.match(condicion, texto)
    if match:
        print('El texto no empieza con la letra R')
    else:
        print('El texto empieza con la letra R')


def alternativas():
    texto='ABC123 abc456'
    condicion=r'[A-Z]{3}[0-9]{3}|[a-z]{3}[0-9]{3}'
    contras= re.findall(condicion, texto)
    for contra in contras:
        print(contra)

def agrupacion():
    texto='Mi nombre es Matias, tengo 19 años'
    condicion=r'([a-z]{6}|[0-9]{2})'
    palabras=re.findall(condicion, texto)
    for palabra in palabras:
        print(palabra)

def repeticionCaracteres():
    texto='111282333 556677'
    condicion=r'([0-3]+)'
    numeros=re.findall(condicion, texto)
    for numero in numeros:
        print(numero)

def cantExacta():
    texto='127346512671829'
    condicion=r'[6-7]{2}'
    numeros=re.findall(condicion, texto)
    for numero in numeros:
        print(numero)

def escape():
    texto='Mi nombre es Matias. Mis cuentas de banco estan en: $100000 pesos'
    condicion=r'\$[0-9]+'
    numeros=re.findall(condicion, texto)
    for numero in numeros:
        print(numero)

def main():
    posicionInicioYFin()
    cualquierCaracter()
    claseCaracteres()
    negacionComienzo()
    alternativas()
    agrupacion()
    repeticionCaracteres()
    cantExacta()
    escape()
main()