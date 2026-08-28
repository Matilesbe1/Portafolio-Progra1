import funciones

def main():
    tupla=funciones.cargar_productos()
    #funciones.mostrar_producto(tupla)
    #funciones.buscar_producto(tupla)
    promedio= funciones.precio_promedio(tupla)
    funciones.producto_mayor_precio(tupla)
main()