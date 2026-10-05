'''8. Integración con matrices
Una empresa registra las unidades vendidas de tres productos durante cuatro semanas. Los códigos de producto se almacenan en una tupla y las cantidades en una matriz de 3 x 4, donde cada fila corresponde al producto ubicado en la misma posición de la tupla.

Desarrollen funciones para: 
a) Informar el total vendido por producto. 
b) Informar el total de una semana indicada.
c) Determinar el código del producto con mayor venta acumulada. 
d) Validar la semana ingresada y capturar los errores correspondientes.'''

def total_producto(matriz):
    '''Recibe la matriz de las ventas y devuelve una lista con las sumas de los totales por prodcutos'''
    fil = len(matriz)
    col = len(matriz[0])
    suma = 0
    totales = []
    for f in range(fil):
        suma = 0
        for c in range(col):
            suma += matriz[f][c]
        totales.append(suma)
    return totales

def mostrar_totales(totales,codigos):
    '''Recibe la lista de los totales y la tupla de codigos y los muestra con formato por pantalla'''
    print(f"{"-"*5} TOTALES {"-"*5}")
    for i in range(len(totales)):
        print(f"{codigos[i]} -> {totales[i]}")

def totales_semana(matriz,sem):
    '''Recibe la matriz y una semana indicada entre 1 y 4 y retorna la suma de las ventas de esa semana'''
    suma = 0
    for f in range(len(matriz)):
        suma += matriz[f][sem]
    return suma

def pedir_semana():
    '''Pide al usuario que indique la semana correspondiente a la funcion totales_semana()'''
    semana = int(input("Ingrese la semana deseada: "))
    while semana < 1 or semana > 4:
        print("Error. Las semanas van de 1 a 4.")
        semana = int(input("Intene nuevamente: "))
    return semana

def max_producto(totales,codigos):
    '''Recibe los totales y los codigos y retorna una lista con el/los elementos con mayor venta.'''
    mayor_vta = max(totales)
    i_max = totales.index(mayor_vta)
    maximos = [codigos[i] for i in range(len(codigos)) if totales[i]==totales[i_max]]
    return maximos

def mostrar_max(maximos):
    '''Recibe al lista de maximos y la muestra con formato por pantalla'''
    for x in maximos:
        print("->",x,end=" ")

def main():
    codigos = ("P101", "P205", "P330") 
    ventas_semanales = [ [12, 15, 10, 18], [20, 17, 22, 19], [20, 17, 22, 19] ]

    semana = pedir_semana()-1
    lst_totales = total_producto(ventas_semanales)
    total_sem = totales_semana(ventas_semanales,semana)
    lst_maximos = max_producto(lst_totales,codigos)

    print(f"El total de la semana {semana+1} es de {total_sem}.")
    mostrar_totales(lst_totales,codigos)
    print(f"Prodcuto(s) con más venta(s): ")
    mostrar_max(lst_maximos)

if __name__ == "__main__":
    main() 