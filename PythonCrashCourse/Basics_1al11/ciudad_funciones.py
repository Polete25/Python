
def ciudad_funciones(ciudad,pais,pob=''):
    if pob:
        full_ciudad = f'{ciudad}, {pais} - {pob} hab.'
    else:
        full_ciudad = f'{ciudad}, {pais}'
     
    return full_ciudad.title()
 