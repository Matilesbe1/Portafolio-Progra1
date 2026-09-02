suma = 0
cont = 0
while True:
    numero = int(input("Ingrese un numero (-1 finalizar): "))
    if numero == -1 and cont == 0:
        print ("No hay datos para calcular el promedio ")
        continue
    elif numero == -1:
        break

    suma += numero
    cont += 1

print (f"Se ingresaron {cont} numeros, y la suma total es {suma}")
print (f"El promedio es {suma/cont}")


