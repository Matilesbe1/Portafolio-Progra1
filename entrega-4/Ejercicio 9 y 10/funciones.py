def cargar_productos():
    primera=True
    tupla=()
    codigo=input('ingrese el codigo del producto: ')
    while codigo.lower()!='fin':
        while not codigo.isdigit():
            codigo=input('ingrese un codigo correcto: ')
        descripcion=input('ingrese la descripcion del producto: ')
        precio=(input('ingrese el precio del producto: '))
        while not precio.isdigit():
            precio=(input('ingrese un precio correcto: '))
        producto=(codigo, descripcion, precio)
        tupla+=(producto, )
        primera=False
        if primera==False:
            codigo=(input('ingrese el codigo del producto: '))
    print(tupla)
