def pedirNumero():
    try:
        numero = int(input("Ingrese un número: "))
        if numero != 0:
            resultado = 100 / numero
            print(resultado)
        else:
            print ("No se puede dividir por 0")
    except ValueError:
        numero=int(input('indique un valor entrero: '))

def capturarPosicion():
    try:
        numeros=[1, 2, 3, 4, 5, 6]
        print(numeros)
        posicion=int(input('posicion: '))
        if posicion<0:
            raise ValueError('ERROR:')
        print(numeros[posicion])
    except ValueError:
        print('ERROR: dato no valido. ')
    except IndexError:
        print('ERROR: Posicion erronea')

def capturarNumeros():
    try:
        n1=int(input('ingrese un numero: '))
        n2=int(input('ingrese otro numero:'))
    except ValueError:
        print('ERROR: Dato no valido')
    except ZeroDivisionError:
        print('ERROR: Se quiso dividir por 0')
    else:
        print(n1/n2)
    finally:
        print('Muchas gracias por probar el programa')
