def es_primo(numero):
    if numero < 2:
        return False

    primo = True
    for divi in range (2, numero):
        if numero % divi == 0:
            primo = False
            break

    return primo

def main():
    nro = int(input("Ingrese un numero: "))
    respuesta = es_primo(nro)
    print (f"¿el numero {nro} es primo? {respuesta}")
main()
