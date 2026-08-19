
def mostrarCatalogo(juegos):
    cont = len(juegos)

    print("\n========== CATÁLOGO DE VIDEOJUEGOS ==========")

    for i in range(len(juegos)):
        print(f"{i + 1}. {juegos[i]}")

    print("=============================================")
    print(f"Total de elementos: {cont}")

def buscarTitulo(juegos):
    busqueda=input('ingrese un titulo que quiere buscar en la lista: ')
    encontrado=False
    for juego in juegos:
        if juego.lower()==busqueda.lower():
            encontrado=True
    if encontrado==True:
        print('Ese titulo esta en la lista')
    else:
        print('ese titulo no se encuentra en la lista')

def agregarTitulo(juegos):
    agreg=(input('ingrese el titulo de videojuego que quiere agregar: '))
    while agreg.lower() in [juego.lower() for juego in juegos]:
        print(f'ese titulo ya se encuentra en la lista ')
        agreg=(input('ingrese el titulo de videojuego que quiere agregar: '))
    juegos.append(agreg)
    print(f'ya se añadio a la lista el titulo: {agreg}')
    return juegos



def mostrarTitulos(juegos):
    print("\n========== PRIMEROS 5 TITULOS ==========")
    print(f'{juegos[:5]}')
    ("=============================================")

    print("\n========== ULTIMOS 3 TITULOS ==========")
    print(f'{juegos[-3:]}')
    ("=============================================")

    print("\n========== LISTA INVERSA ==========")
    print(f'{juegos[::-1]}')
    ("=============================================")

def crearLista8Caracteres(juegos):
    lstNueva=[]
    for juego in juegos:
        if len(juego)>8:
            lstNueva.append(juego)
    print("\n========== LISTA 8 CARACTERES ==========")
    print(lstNueva)
    ("=============================================")

def lambdaFuncion(juegos):
    lstNueva=list(filter(lambda juego: len(juego)>10, juegos))
    return lstNueva

