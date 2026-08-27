def cargar_productos():
    primera=True
    tupla=()
    codigo=input('ingrese el codigo del producto: ')
    while codigo.lower()!='fin':
        codigo=validarCodigoRepetido(tupla, codigo)
        descripcion=input('ingrese la descripcion del producto: ')
        precio=(input('ingrese el precio del producto: '))
        while not precio.isdigit():
            precio=(input('ingrese un precio correcto: '))
        producto=(codigo, descripcion, precio)
        tupla+=(producto, )
        primera=False
        if primera==False:
            codigo=(input('ingrese el codigo del producto: '))
    return tupla

def validarCodigoRepetido(tupla, codigo):
    while not codigo.isdigit():
        codigo=input('ingrese un codigo correcto: ')
    for producto in tupla:
        codigoN, descripcion, precio=producto
        while codigoN==codigo:
            codigo=input('ese codigo esta repetido, intente con otro: ')
            while not codigo.isdigit():
                codigo=input('ingrese un codigo correcto: ')
    return codigo

def mostrar_producto(tupla):
    for producto in tupla:
        codigo, descripcion, precio=producto
        print(f'codigo: {codigo}. descripcion: {descripcion}. precio: ${precio}')

def buscar_producto(tupla):
    if not tupla: 
        return 
    busca=input('ingrese el codigo del producto que quiere buscar: ')
    encontrado=False
    for producto in tupla:
        codigo, descripcion, precio=producto
        if busca==codigo and encontrado==False:
            print(f'Producto encontrado: codigo:{codigo}, descripcion: {descripcion}, precio:${precio}')
            encontrado=True
    if encontrado==False:
        print('no existe el producto con ese codigo :)')

def producto_mayor_precio(tupla):
    max=0
    if not tupla:
        return 
    for producto in tupla:
        if producto[2]>max:
            max=producto[2]
    for producto in tupla:
        if producto[2]==max:
            codigo, descripcion, precio=producto
            print(f'Producto encontrado: codigo:{codigo}, descripcion: {descripcion}, precio:${precio}')


def precio_promedio(tupla):
    suma=0
    promedio=0
    if not tupla:
        return
    for producto in tupla:
        codigo, descripcion, precio=producto
        suma+=int(precio)
    promedio=suma/len(tupla)
    return promedio

