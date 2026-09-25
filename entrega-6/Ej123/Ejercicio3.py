import re
def validarContraseña(contra):
    patron=r'[A-Z]{2}[0-9]{4}'
    match=re.match(patron, contra)
    if match:
        print('la contraseña es valida')
    else:
        print('la contraseña es invalida')

def validarLegajo(legajo):
    patron=r'[0-9]{5}'
    match=re.match(patron, legajo)
    if match:
        print('legajo valido')
    else:
        print('legajo invalido')

def importe(importe):
    patron=r'\$+'
    match=re.match
    if match:
        print (f'el valor es: {importe}')
    else:
        print('valor invalido')

def palabra(palabra):
    patron=r'[A-Z]{1}[a-z]+'
    match=re.match(patron, palabra)
    if match:
        print('palabra valida')
    else:
        print('palabra invalida')

def fecha(fecha):
    patron=r'[0-9]{2}/[0-9]{2}/[0-9]{4}'
    match=re.match(patron, fecha)
    if match:
        print('fecha valida')
    else:
        print('fecha invalida')

def main():
    validarContraseña('AB1234')
    validarLegajo('12345')
    importe('$5000')
    palabra('Matias')
    fecha('24/11/1999')
main()