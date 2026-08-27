import funciones

def main():
    tupla=funciones.cargar_productos()
    funciones.mostrar_producto(tupla)
    promedio= funciones.precio_promedio(tupla)
main()