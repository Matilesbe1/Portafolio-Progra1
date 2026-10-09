import funciones

def main():
    try: 
        with open('productos.csv', mode='wt') as arch:
            funciones.crearCSV(arch)
            arch.close()
            funciones.calcularImporte()
    except (OSError, ValueError):
        print('ERROR: Hubo un error en el sistema')


main()