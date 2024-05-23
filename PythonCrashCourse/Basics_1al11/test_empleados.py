import pytest
from empleados import Empleados

def test_dar_aumento_predereminado():
    empleado1 = Empleados("Pol","Alomar",50000)
    empleado1.dar_aument()
    assert 55000 == empleado1.salario

def test_dar_aumento_personalizado():
    empleado1 = Empleados("Pol","Alomar",50000)
    aumento = 10000
    empleado1.dar_aument(aumento)
    assert 60000 == empleado1.salario