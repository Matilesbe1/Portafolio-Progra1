"""
Desarrollar un programa para gestionar las entregas del Proyecto Integrador mediante entregas.csv. Cada registro 
contendrá número de grupo, nombre del proyecto, integrante responsable y porcentaje de avance.

Dividan la solución en funciones para:
a) Crear el archivo y escribir una única fila de encabezado.
b) Cargar entregas sin repetir el número de grupo.
c) Mostrar todas las entregas válidas.
d) Buscar una entrega por número de grupo.
e) Informar los proyectos con avance inferior al 50 %.
f) Calcular el promedio de avance sin dividir por cero cuando no haya registros válidos.
g) Informar y omitir registros mal formados sin interrumpir todo el procesamiento.
Validen que el número de grupo sea positivo, que los campos de texto no estén vacíos y que el porcentaje se encuentre 
entre 0 y 100. Procesen el archivo una sola vez por operación y eviten cargarlo completo en memoria cuando no sea 
necesario.
"""


def crear_archivo (nombre_Archivo):
    try:
        arch = open(nombre_Archivo , "wt")
    except OSError:
        print ("Error, no se pudo crear correctamente el archivo")
    else:
        arch.write ("Numero del grupo;Nombre proyecto;Integrante responsable;Porcentaje de avance\n")
        arch.close()
        print("¡Archivo creado con exito!")


def existeGrupo (nombre_Archivo, nro_grupo):
    try:
        arch = open(nombre_Archivo, "rt")
    except OSError:
        return False
    else: 
        arch.readline() #descarto el encabezado
        for linea in arch:
            datos = linea.rstrip("\n").split(";")
            if len(datos) == 4 and datos[0].isdigit():
                if int(datos[0]) == nro_grupo:
                    arch.close()
                    return True

        arch.close()
        return False


def validacion_desempaquetacion(linea):
    datos = linea.rstrip("\n").split(";")
    if len(datos) != 4:
        return None

    n_grupo,proyecto,integrante,p_avance = datos

    if not proyecto.strip() or not integrante.strip():
        return None

    try:
        grupo = int(n_grupo)
        avance = float(p_avance)
    except ValueError:
        return None

    if grupo <= 0 or not (0 <= avance <= 100):
        return None

    return grupo, proyecto.strip(), integrante.strip(), avance



def cargar_entrega(nombre_archivo):
    """b) Cargar entregas sin repetir el número de grupo."""
    print("\n--- Carga de Entrega ---")
    try:
        grupo = int(input("Ingrese número de grupo: "))
        if grupo <= 0:
            print("El número de grupo debe ser positivo.")
            return
    except ValueError:
        print("Debe ingresar un número entero válido.")
        return

    if existeGrupo(nombre_archivo, grupo):
        print(f"El grupo {grupo} ya se encuentra registrado.")
        return

    proyecto = input("Nombre del proyecto: ").strip()
    integrante = input("Integrante responsable: ").strip()

    if not proyecto or not integrante:
        print("El nombre del proyecto y el integrante no pueden estar vacíos.")
        return

    try:
        avance = float(input("Porcentaje de avance (0 a 100): "))
        if not (0 <= avance <= 100):
            print("El porcentaje debe estar entre 0 y 100.")
            return
    except ValueError:
        print("El porcentaje debe ser un valor numérico.")
        return

    # abrimos el archivo en modo agregar ("at")
    try:
        arch = open(nombre_archivo, "at")
    except OSError:
        print("Error al abrir el archivo para agregar el registro.")
    else:
        arch.write(str(grupo) + ";" + proyecto + ";" + integrante + ";" + str(avance) + "\n")
        arch.close()
        print("Entrega registrada con éxito.")


def mostrar_entregas(nombre_archivo):
    """c) y g) Mostrar entregas válidas e informar registros mal formados."""
    print("\n--- Lista de Entregas Válidas ---")
    try:
        arch = open(nombre_archivo, "rt")
    except OSError:
        print("No se pudo abrir el archivo.")
    else:
        arch.readline()  
        nro_linea = 1

        for linea in arch:
            nro_linea += 1
            registro = validacion_desempaquetacion(linea)
            if registro is not None:
                grupo, proyecto, integrante, avance = registro
                print(f"Grupo {grupo} | Proyecto: {proyecto} | Resp: {integrante} | Avance: {avance}%")
            else:
                print(f"Línea {nro_linea} descartada por formato incorrecto: {linea.rstrip('\n')}")

        arch.close()


def buscar_entrega(nombre_archivo):
    """d) Buscar una entrega por número de grupo."""
    try:
        buscado = int(input("\nIngrese el número de grupo a buscar: "))
    except ValueError:
        print("Número inválido.")
        return

    try:
        arch = open(nombre_archivo, "rt")
    except OSError:
        print("No se pudo abrir el archivo.")
    else:
        arch.readline()  
        encontrado = False

        for linea in arch:
            registro = validacion_desempaquetacion(linea)
            if registro is not None:
                grupo, proyecto, integrante, avance = registro
                if grupo == buscado:
                    print(f"\nGrupo encontrado:")
                    print(f"Proyecto: {proyecto}")
                    print(f"Responsable: {integrante}")
                    print(f"Avance: {avance}%")
                    encontrado = True
                    break

        arch.close()

        if not encontrado:
            print(f"No se encontró ninguna entrega para el grupo {buscado}.")


def informar_avance_menor(nombre_archivo):
    """e) Informar los proyectos con avance inferior al 50%."""
    print("\n--- Proyectos con avance inferior al 50% ---")
    try:
        arch = open(nombre_archivo, "rt")
    except OSError:
        print("No se pudo abrir el archivo.")
    else:
        arch.readline()  # Descartamos el encabezado
        hay_alguno = False

        for linea in arch:
            registro = validacion_desempaquetacion(linea)
            if registro is not None:
                grupo, proyecto, integrante, avance = registro
                if avance < 50:
                    print(f"Grupo {grupo} - '{proyecto}' (Avance: {avance}%)")
                    hay_alguno = True

        arch.close()

        if not hay_alguno:
            print("No hay proyectos con avance menor al 50%.")


def calcular_promedio(nombre_archivo):
    """f) Calcular el promedio de avance evitando división por cero."""
    try:
        arch = open(nombre_archivo, "rt")
    except OSError:
        print("No se pudo abrir el archivo.")
    else:
        arch.readline()  
        suma_avance = 0.0
        cant_validos = 0

        for linea in arch:
            registro = validacion_desempaquetacion(linea)
            if registro is not None:
                grupo, proyecto, integrante, avance = registro
                suma_avance += avance
                cant_validos += 1

        arch.close()

        if cant_validos > 0:
            promedio = suma_avance / cant_validos
            print(f"\nPromedio general de avance ({cant_validos} entregas válidas): {promedio:.2f}%")
        else:
            print("\nNo se puede calcular el promedio: no existen registros válidos en el archivo.")


def main():
    nombre_archivo = "entregas.csv"

    while True:
        print("\n==================================")
        print("    GESTIÓN DE ENTREGAS (CSV)     ")
        print("==================================")
        print("1. Crear archivo con encabezado")
        print("2. Cargar nueva entrega")
        print("3. Mostrar entregas válidas")
        print("4. Buscar entrega por grupo")
        print("5. Informar avance menor al 50%")
        print("6. Calcular promedio general de avance")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()
        print ("="*35)

        if opcion == "1":
            crear_archivo(nombre_archivo)
            input("\nIntroduzca espacio para continuar")

        elif opcion == "2":
            cargar_entrega(nombre_archivo)
            input("\nIntroduzca espacio para continuar")

        elif opcion == "3":
            mostrar_entregas(nombre_archivo)
            input("\nIntroduzca espacio para continuar")
        elif opcion == "4":
            buscar_entrega(nombre_archivo)
            input("\nIntroduzca espacio para continuar")

        elif opcion == "5":
            informar_avance_menor(nombre_archivo)
            input("\nIntroduzca espacio para continuar")

        elif opcion == "6":
            calcular_promedio(nombre_archivo)
            input("\nIntroduzca espacio para continuar")

        elif opcion == "0":
            print("Fin del programa.")
            break
        else:
            print("Opción inválida. Ingrese una opción del menú.")


main()
