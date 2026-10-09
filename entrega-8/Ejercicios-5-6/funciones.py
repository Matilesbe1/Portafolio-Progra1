def crearCSV():
    arch=open('productos.csv', mode='wt')
    #codigo, descripcion, cantidad, precio
    cargarCodigoCSV(arch)
    return arch

def cargarCodigoCSV(arch):
    n=input('ingrese el codigo del producto que quiere cargar (FIN para finalizacion): ').upper()
    while n!='FIN':
        arch.write(n+';')
        cargarDescripcionCSV(arch)
        cargarCantidadCSV(arch)
        cargarPrecioCSV(arch)
        n=input('ingrese el codigo del producto que quiere cargar (FIN para finalizacion): ').upper()

def cargarDescripcionCSV(arch):
    des=input('ingrese la descripcion del producto: ')
    arch.write(des+';')

def cargarCantidadCSV(arch):
    cant=int(input('ingrese la cantidad de productos comprados: '))
    while cant<0:
        cant=int(input('ingrese una cantidad correcta: '))
    arch.write(str(cant)+';')

def cargarPrecioCSV(arch):
    prec=int(input('ingrese el precio unitario: '))
    while prec<=0:
        prec=int(input('ingrese un precio correcto: '))
    arch.write(str(prec)+ '\n')

def calcularImporte():
    arch=open('productos.csv', mode='rt')
    importe=0
    importe_final=0
    cant=0
    for linea in arch:
        codigo, descripcion, cantidad, precio =linea.split(';')
        importe=int(cantidad)*int(precio)
        importe_final=calcularImporteFinal(importe, importe_final)
        cant=cantidadMenor(cantidad, cant)
        print(f'importe del producto con el ID {codigo}: {importe}')
    print(f'importe final: {importe_final}')
    print(f'Hay {cant} productos con la cantidad comprada menor a 5')
    arch.close()

def calcularImporteFinal(importe, importe_final):
    importe_final=importe_final+importe
    return importe_final

def cantidadMenor(cantidad, cant):
    if int(cantidad)<5:
        cant+=1
    return cant