import random

def recaudacion_sucursal(matriz):
    resultado=[]
    for i in range (len(matriz)):
        resultado.append(sum(matriz[i]))
    return resultado

def mayor(resultado):
    mayor=resultado[0]
    i=0
    for i in range (len(resultado)):
        if mayor<resultado[i]:
            mayor=resultado[i]
            i=[i]
    print(f'el dia con mayor recaudacion, fue el dia num {i}')

def recaudacion_dia(matriz):
    resultado = []
    for j in range(len(matriz[0])):
        columna = []
        for i in range(len(matriz)):
            columna.append(matriz[i][j])
        resultado.append(sum(columna))
    return resultado

def recaudacion_general(lst):
    suma=sum(lst)
    return suma

def carga_Valores(cont):
    valor=int(input(f'ingrese la recaudacion de multas de la sucursal num {cont}: '))
    while valor<0:
        valor=int(input('ingrese una recaudacion correcta: '))
    return valor

def crearMatriz(filas, columnas):
    cont=0
    matriz=[]
    for i in range (filas):
        matriz.append([])
        cont+=1
        for j in range (columnas):
            valor=carga_Valores(cont)
            matriz[i].append(valor)
    return matriz

def main():
    sucursales=4
    semana=7
    matriz=crearMatriz(sucursales, semana)

    for i in range (len(matriz)):
        print(matriz[i])
    rec_sucursal=recaudacion_sucursal(matriz)
    rec_dia=recaudacion_dia(matriz)
    print(f'recaudacion de cada sucursal: {rec_sucursal}')
    print(f'recaudacion de cada dia: {rec_dia}')
    print(f'recaudacion general: {recaudacion_general(rec_sucursal)}')
    mayor(rec_dia)
main()