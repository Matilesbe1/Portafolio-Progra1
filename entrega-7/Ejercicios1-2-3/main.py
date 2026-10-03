def agregarTecnologia(tecnologias):
    t=input('ingrese una tecnologia a la lista: ')
    tecnologias.add(t)
    print(f'lista de tecnologias: {tecnologias}')

def eliminarTecnologiaRemove(tecnologias, tec):
    tecnologias.remove(tec)
    print(f'lista eliminada con Remove {tecnologias}')

def eliminarTecnologiaDiscard(tecnologias, tec):
    tecnologias.discard(tec)
    print(f'lista eliminada con Discard {tecnologias}')

def tecnologiasIncluidas(tecnologias):
    obligatorias={'Java', 'Python'}
    if obligatorias.issubset(tecnologias):
        print('Inluido issubset')
    if tecnologias.issuperset(obligatorias):
        print('Incluido issuperset')
    

def vaciarConjunto(tecnologias):
    tecnologias_2=tecnologias.copy()
    print(tecnologias_2.clear())

def main():
    tecnologias={'Python', 'Java', 'HTML', 'CSS', 'JavaScript'}
    try:
        agregarTecnologia(tecnologias)
        tecnologiasIncluidas(tecnologias)
        eliminarTecnologiaDiscard(tecnologias, 'Css')
        eliminarTecnologiaRemove(tecnologias, 'Python')
        eliminarTecnologiaRemove(tecnologias, 'C')
        vaciarConjunto(tecnologias)
    except:
        KeyError('ERROR: Hubo un error de tipo KeyError')

main()