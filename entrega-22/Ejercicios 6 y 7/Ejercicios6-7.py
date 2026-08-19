'''
6. Listas por compresion
Construyan nuevas listas sin utilizar append(). Distingan entre una transformacion, un filtro y una expresion condicional.'''

puntajes= [45,80,63,91,100,72]

'''A) Crear una lista con todos los puntajes duplicados.'''
# Es una transformacion
duplicados=[p*2 for p in puntajes]

'''B) Crear una lista que contenga solamente los puntajes aprobados (60 o mas).'''
# Es un filtro
aprobados=[p for p in puntajes if p>=60]

'''C) Crear una lista con el cuadrado de los valores pares.'''
# Es un filtro y una transformacion 
cuadrado=[p**2 for p in puntajes if p%2==0]

'''D) Crear una lista con el texto "Aprobado" o "Revisar" segun cada puntaje.'''
# Es una expresion condicional
nueva=["Aprobado" if p>=60 else "Revisar" for p in puntajes]

'''E) Explicar porque la lista original no se modifica'''
#Porque solo lee los elementos de puntajes pero no se le aplica el append() ni nada, segun el ejercicio se le aplican filtros o transformaciones pero se guardan en una lista nueva sin tocar a la original.


'''
7. Funciones lambda
Definan y prueben las siguientes funciones lambda:'''

'''A) Cuadrado: retorna el cuadrado de un numero'''
cuadrado= lambda n: n**2
print(cuadrado(5))

'''B) Es_par: retorna True cuando el numero es par'''
es_par= lambda n: n%2==0
print(es_par(8))

'''C) Mayor: retorna el mayor entre dos numeros'''
mayor= lambda a,b: a if a>b else b
print(mayor(5,4))

'''D) Aplicar_descuento: aplica un descuento porcentual a un precio'''
aplicar_descuento= lambda a,b: a-a*b/100
print(aplicar_descuento(800,5))

'''E) Indiquen cual de ellas escribirian con def en un programa real y justifiquen'''
# La funcion que escribiria con def en un programa real es aplicar_descuento porque necesitaria validaciones y las funciones lambda no permiten hacerlas como tampoco permiten instrucciones multiples, solo una expresion simple.