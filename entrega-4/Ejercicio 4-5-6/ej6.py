dia = 25
mes = "Septiembre"
año = 2026
fecha = dia, mes, año
dia_nac, mes_nac, año_nac = fecha
# PUNTO A
# Es una tupla sin parentesis porque son variables simples que estan siendo empaquetadas.
# PUNTO B
print(dia_nac)
print(mes_nac)
print(año_nac)
# PUNTO C
var1, var2 = fecha
print(fecha)
# ValueError: too many values to unpcack(expected 2), esto es debido a que no hay la misma cantidad de variables que elementos en la tupla.
# PUNTO D
# Deben tener la misma cantidad de elementos que de variables