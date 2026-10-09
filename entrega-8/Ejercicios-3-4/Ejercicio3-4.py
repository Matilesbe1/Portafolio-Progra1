'''3. Escritura de registros de texto
Desarrollar una función crear_alumnos() que genere alumnos.txt. Por cada alumno se ingresarán legajo, nombre y
apellido, y comisión. La carga finalizará con un legajo igual a -1; ese valor de corte no debe grabarse.
Cada registro debera almacenarse en una linea con sus campos separados por punto y coma. Antes de escribir, validen
que el legajo sea positivo, que el nombre no esté vacío y que la comisión tenga un formato válido (valor numérico de 1 a
10).
Prueben la función con varios alumnos. Luego ejecutenla nuevamente usando modo "wt" y expliquen que ocurrió con los
datos anteriores. Repitan con modo "at" y comparen los resultados.'''

def crear_alumnos():
    try:
        archivo = open('alumnos.txt', mode="at")
    except OSError:
            print("Error al abrir el archivo")
    else:
        legajo = int(input("Ingrese el legajo del alumno (-1 para terminar): "))
        while legajo < 0 and legajo != -1:
            print("Debe ser positivo. Vuelva a ingresarlo")
            legajo = int(input("Ingrese el legajo del alumno (-1 para terminar): "))
        
        while legajo != -1:     
            nombre_apellido= input("Ingrese el nombre y el apellido del alumno: ")
            while nombre_apellido == "":
                print("Debe completar el nombre y el apellido. Vuelve a ingresarlo")
                nombre_apellido= input("Ingrese el nombre y el apellido del alumno: ")
            
            comision = int(input("Ingrese la comision (1-10): "))
            while comision < 1 or comision > 10: 
                print("Debe estar entre 1 y 10. Vuelve a ingresarlo")
                comision = int(input("Ingrese la comision (1-10): "))
        
            archivo.write(str(legajo) + ";" + nombre_apellido + ";" + str(comision) + "\n")
            legajo = int(input("Ingrese el legajo del alumno (-1 para terminar): "))
        archivo.close()
def main():
    crear_alumnos()
if __name__ == '__main__':
    main()

'''4. Lectura y procesamiento secuencial
Desarrollar mostrar_alumnos() para leer alumnos.txt registro por registro, sin cargar el archivo completo en memoria.
Para cada linea deberan eliminar solamente el salto de linea final, separar los campos y verificar que el registro tenga
exactamente tres campos antes de convertir el legajo.

Resolver:
a) Mostrar todos los registros validos.
b) Informar solo los alumnos cuyo legajo sea mayor a 10000.
c) Contar cuantos alumnos pertenecen a cada comisión mediante un diccionario.
d) Registrar o informar las lineas que no respeten el formato esperado.
Utilicen rstrip("\n") en lugar de strip() cuando solo necesiten quitar el salto de linea, ya que strip() tambien elimina
espacios al comienzo y al final del texto.'''

def mostrar_alumnos():
    try:
        archivo = open('alumnos.txt', mode="rt")
    except OSError:
        print("Hubo un error al abrir el archivo")
    else:
        dic = {}
        no_respetan_formato = 0
        for linea in archivo:
            try:
                legajo, nombre_apellido, comision = linea.rstrip("\n").split(";")
                legajo = int(legajo)
                comision = int(comision)
            except ValueError:
                print("Registro invalido")
                no_respetan_formato += 1
            else: 
                print(f"Legajo: {legajo} - Nombre y apellido: {nombre_apellido} - Comision: {comision}")
                if legajo > 10000:
                    print(f"El alumno {nombre_apellido} tiene un legajo mayor a 10000")
                if comision not in dic:
                    dic[comision] = 0
                dic[comision] += 1
        for i in dic:
            print(f"Comision: {i} - Cantidad de alumnos {dic[i]}")
        print(f"La cantidad de lineas que no respetan el formato esperado son de: {no_respetan_formato}")
        archivo.close()
