codigos = [101, 103, 101, 105, 103, 108]


def codigos_unicos(codigos):
    unicos = set(codigos)
    return unicos

unicos = codigos_unicos(codigos)

#a) Informen cuántos códigos distintos hay.
print(f"Hay {len(unicos)} codigos distintos")
#b) Verifiquen si el código 105 fue informado.
if 105 in unicos:
    print("Fue informado")
else:
    print("No fue informado")
#c) Conviertan el conjunto en una lista ordenada para mostrar un resultado predecible.
lista_ordenada = list(unicos)
lista_ordenada.sort()
print(lista_ordenada)
#d) Expliquen qué información se pierde al convertir directamente una lista en conjunto.
# La informacion que se pierde al convertir una lista en conjunto es el orden original de los elementos y los elementos duplicados.
