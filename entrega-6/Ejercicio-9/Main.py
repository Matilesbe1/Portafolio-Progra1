"""
Desarrollen un formulario que solicite nombre, legajo, correo electrónico, teléfono y código de comisión. Antes de 
programar, definan y documenten el formato exacto de cada dato, especialmente el código de comisión.

El programa deberá:
• Validar el formato completo mediante funciones independientes.
• Mostrun par un mensaje espcífico cuando un dato no cumpla el patrón.
• Volver a solicitar cada dato hasta obtener un valor válido.
• Mantener separadas la entrada de datos, la validación y la presentación de resultados.
• Mostrar al finalizar todos los datos registrados.
• Incluir rograma principal y un módulo validaciones.py.
• Código fuente de todos los ejercicios y del módulo validaciones.py.
• Tabla con cada patrón, su interpretación, alcance y ejemplos válidos e inválidos.
• Capturas de ejecución de match(), search(), fullmatch(), findall(), finditer(), sub() y split().
• Comparación entre búsqueda parcial y validación completa.

"""
import validaciones

def entradaDatos():
    print ("\n========== INGRESO DE DATOS ==========")

    nombre = input("Ingrese el nombre del estudiante: ").title()
    while not validaciones.validacionNombre(nombre):
        print ("\nError, ingrese un nombre valido")
        nombre = input("Ingrese el nombre del estudiante: ").title()

    legajo = input("Ingrese su legajo: ")
    while not validaciones.validacionLegajo(legajo):
        print ("\nError, el legajo contiene unicamente digitos")
        legajo = input("Ingrese legajo:")

    correo = input("Ingrese su correo: ")
    while not validaciones.validacionCorreo(correo):
        print ("\nError, ingrese un correo valido")
        correo = input("Ingrese su correo:")

    telefono = input("Ingrese su numero de telefono:")
    while not validaciones.validacionTelefono(telefono):
        print ("\nError, ingrese un numero valido (10 digitos)")
        telefono = input("Ingrese su numero de telefono:")

    comision = input("Ingrese su comision:").upper()
    while not validaciones.validacionComision(comision):
        print ("Error, ¡recuerda el formato! (ABC-123)")
        comision = input("Ingrese su comision:").upper()

    print ("=" *39)
    return nombre,legajo,correo,telefono,comision

def main():
    nombreUsuario,legajoUsuario,correoUsuario,telefonoUsuario,comisionUsuario = entradaDatos()

    print ("\n========== DATOS DEL USUARIO ==========")
    print (f"Nombre del usuario: {nombreUsuario}")
    print (f"Legajo del usuario: {legajoUsuario}")
    print (f"Correo del usuario: {correoUsuario}")
    print (f"Numero de telefono del usuario: {telefonoUsuario}")
    print (f"La comision del usuario: {comisionUsuario}")
    print ("=" * 39)
main()