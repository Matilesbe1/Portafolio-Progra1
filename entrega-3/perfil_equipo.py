""""
Desarrollen perfil_equipo.py dentro de la carpeta codigo del repositorio. El programa deberá solicitar el nombre del
equipo, comisión, nombre de cada integrante y rol inicial en el proyecto.
El programa deberá:
• Normalizar los nombres con title().
• Convertir el nombre del equipo a mayúsculas.
• Informar la cantidad de caracteres del nombre del equipo.
• Generar una sigla con la inicial de cada palabra.
• Verificar si el nombre del equipo contiene al menos un dígito recorriendo sus caracteres y utilizando isdigit().
• Mostrar toda la información mediante f-strings.
• Mantener las operaciones de procesamiento dentro de funciones y la entrada/salida general en el programa principal.
def contiene_digitos(texto):
 val= False
 for caracter in texto:
 if caracter.isdigit():
 val= True
 return val
"""
def contiene_digitos(equipo):
    val = False
    for caracter in equipo:
        if caracter.isdigit():
            val = True
    return val

def generarSigla (nombreEquipo):
    listaPalabras = nombreEquipo.split()
    sigla = ""
    for palabra in listaPalabras:
        sigla = sigla + palabra[0]
    sigla = sigla.upper()
    return sigla.upper()

def main():
    nombreEquipo = input("Nombre del equipo:").upper()
    comision = input ("Introduzca la comision: ")
    cantidad = int(input("Ingrese la cantidad de integrantes del equipo: "))
    integrantes = []
    roles = []

    #Con la cantidad de los integrantes creamos un ciclo y agregamos los nombres y roles a las listas vacias
    for i in range (cantidad):
        nombreIntegrante = input("Ingresar nombre: ").title()
        rolEquipo = input("Ingrese el rol inicial en el proyecto: ")

        integrantes.append(nombreIntegrante)
        roles.append(rolEquipo)

    print("\n--- DATOS DEL EQUIPO ---")
    print (f"Los integrantes de {nombreEquipo} son: {integrantes}")
    print (f"la sigla del equipo: {generarSigla(nombreEquipo)}")
    print (f"La cantidad de caracteres que contiene {nombreEquipo} son: {len(nombreEquipo)}")

#llama a la funcion e imprime si tiene o no digitos
    if contiene_digitos(nombreEquipo):
        print (f"El nombre del equipo {nombreEquipo} contiene digito/s")
    else:
        print(f"El nombre del equipo {nombreEquipo} NO contiene digitos ")

main()


