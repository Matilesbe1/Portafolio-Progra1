import re

def validacionNombre(nombre):
    patronNombre = r"[A-Za-zÑñ]+"
    vNombre = re.fullmatch(patronNombre,nombre)
    return vNombre

def validacionLegajo(legajo):
    patronLegajo = r"[0-9]+"
    vLegajo = re.fullmatch(patronLegajo, legajo)
    return vLegajo

def validacionCorreo(correo):
    patronCorreo = r"[a-zA-Z.0-9]+@[a-zA-Z]+\.[a-zA-Z]+"
    vCorreo = re.fullmatch(patronCorreo, correo)
    return vCorreo

def validacionTelefono(telefono):
    patrontelefono = r"[+]?[0-9]{10}"
    vTelefono = re.fullmatch(patrontelefono, telefono)
    return vTelefono

def validacionComision (comision):
    patronComision = r"[A-Z]{3}-[0-9]{3}"
    vComision = re.fullmatch(patronComision, comision)
    return vComision
