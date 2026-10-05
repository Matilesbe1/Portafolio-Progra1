#7) Provocar una excepción con raise
'''raise permite señalar que un dato no cumple las reglas del problema, aun cuando su tipo sea correcto. Implementen calcular_importe(cantidad, precio) de modo que provoque ValueError si cantidad o precio son menores o iguales a cero. La función deberá retornar cantidad * precio cuando los datos sean válidos.
Desde el programa principal, capturen la excepción y muestren su mensaje utilizando except ValueError as error. Prueben con datos válidos, cantidad cero, precio negativo y entradas no numéricas.'''

def valdida_negativo(valor):
    if valor <= 0:
        return True
    else:
        return False

def calcular_importe(cantidad,precio):
    if valdida_negativo(cantidad) or valdida_negativo(precio):
        raise ValueError("Error. Ha ingresado un valo menor o igual a 0")
    return cantidad*precio

def main():

    while True:
        try:
            cant = int(input("Ingrese la cantidad: "))
            precio = int(input("Ingrese el precio unitario: "))
            break
        except ValueError as error:
            print("Ha ingresado un valor erroneo")
            print(error)
            continue
    try: 
        total = calcular_importe(10,1500)
        assert total > 15000, "El importe no es el esperado."
    except ValueError as err:
        print(err)

    else:
        print(total)
main() 
        