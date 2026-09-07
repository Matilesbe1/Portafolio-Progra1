'''Desarrollen un sistema modular que registre productos en una lista. Cada producto podra almacenarse como una lista con código, descripción, cantidad y precio. La carga finaliza cuando el código ingresado sea "FIN".
El programa deberá:
. Utilizar while True y break para finalizar la carga.
. Capturar ValueError al convertir cantidad y precio.
. Utilizar raise ValueError para rechazar cantidades o precios menores o iguales a cero.
. No incorporar un producto cuando sus datos sean inválidos.
. Calcular el importe de cada producto mediante una función.
. Utilizar assert para comprobar una condición interna del cálculo, no para validar la entrada.
. Informar cantidad de productos, importe total y precio promedio; si no se cargaron productos, evitar la división por cero.
'''

def cargar_lista():
    lista = []
    while True:
        codigo = input("Ingrese el codigo del producto: ")

        try:
            codigo = int(codigo)
        except ValueError:
            if codigo.upper() == 'FIN':
                break
            else:
                print("Debe ser un numero")
                continue

        descripcion = input("Ingrese la descripcion del producto: ")

        while True:
            try:
                cantidad = int(input("Ingrese la cantidad: "))
                if cantidad <= 0:
                    raise ValueError("La cantidad debe ser mayor a 0")
                break
            except ValueError as error:
                print(error)

        while True:
            try:
                precio = int(input("Ingrese el precio: "))
                if precio <= 0:
                    raise ValueError("El precio tiene que ser mayor a 0")
                break
            except ValueError as error:
                print(error)

        lista.append((codigo, descripcion, cantidad, precio))
    return lista


def calcular_importe(lista):
    precio = [c[3] for c in lista]
    cant = [c[2] for c in lista]
    lista_importe = []
    for c in range(len(precio)):
        importe = precio[c] * cant[c]
        assert importe > 0, "El importe no puede ser 0 o negativo"
        lista_importe.append(importe)
    return lista_importe

def informe(lista, lista_importe):
    cantidad = len([c[2] for c in lista])
    precio = sum([c[3] for c in lista])
    print(f"La cantidad de productos ingresados es de: {cantidad}")
    print(f"El importe total es de: {sum(lista_importe)}")
    try:
        promedio = precio / cantidad
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    else:
        print(f"El promedio es de: {promedio}")
    
def main():
    lista = cargar_lista()
    lista_importe = calcular_importe(lista)
    informe(lista, lista_importe)
if __name__ == '__main__':
    main()