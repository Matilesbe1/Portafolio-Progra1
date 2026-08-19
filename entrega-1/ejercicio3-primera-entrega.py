

def solucion(dias_pactados):
    cant=0
    multa=0
    dias=int(input('cuantos dias pasaron desde que se llevo el libro: '))
    if dias>dias_pactados:
        cant=dias-dias_pactados
        multa=800*cant






def fechaPactada():
    dias_pactados=int(input('indique la cantidad de dias que se va a llevar el libro (se le suman $800 por cada dia de atrazo de entrega. Si despues el libro esta reservado, la multa es de $2500): '))
    while dias_pactados<=0:
        dias_pactados=int(input('indique un numero correcto: '))
    return dias_pactados
    


def peticion(lst):
    id_libro_usuario=int(input('escriba el id del libro que quiere: '))
    while id_libro_usuario not in lst:
        id_libro_usuario=int(input('no tenemos ese libro, pruebe con otro: '))
    dias_pactados=fechaPactada()
    print('UNOS DIAS MAS TARDE...')
    solucion(dias_pactados)


def main():
    lst_libros=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    peticion(lst_libros)
main()