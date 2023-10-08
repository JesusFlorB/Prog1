from src.ejercicio6 import calcular_iva, calcular_importe_sin_iva

def test_calcular_iva():
    assert calcular_iva(100, 10) == 10.0
    assert calcular_iva(200, 8) == 16.0

def test_calcular_importe_sin_iva():
    assert calcular_importe_sin_iva(100, 10) == 90.0
    assert calcular_importe_sin_iva(200, 16) == 184.0