from src.ejercicio27 import calcular_costo_total

def test_calcular_costo_total():
    assert calcular_costo_total(10, 5) == 50
    assert calcular_costo_total(8.5, 3) == 25.5