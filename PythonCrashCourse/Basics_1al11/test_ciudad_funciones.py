import pytest
from ciudad_funciones import ciudad_funciones

def test_ciudad_funciones():
    
    ciudadpais = ciudad_funciones('buenos Aires', 'argentina')
    
    assert ciudadpais == "Buenos Aires, Argentina"
    
def test_hab_funciones():
    
    ciudadpais = ciudad_funciones('buenos Aires', 'argentina', '44000000')
    
    assert ciudadpais == "Buenos Aires, Argentina - 44000000 Hab."
    
