import videojuegos

def main():
    juegos = [
    "Minecraft",
    "FIFA",
    "Fortnite",
    "GTA V",
    "Rocket League",
    "Among Us",
    "Call of Duty",
    "Valorant",
    "League of Legends",
    "The Witcher 3"
]
    videojuegos.mostrarCatalogo(juegos)
    videojuegos.buscarTitulo(juegos)
    videojuegos.agregarTitulo(juegos)
    videojuegos.mostrarTitulos(juegos)
    videojuegos.crearLista8Caracteres(juegos)
    videojuegos.lambdaFuncion(juegos)
main()