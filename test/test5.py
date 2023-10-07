from src.ejercicio5 import Total

def test_Total():
    precio = 100
    IVA = 10
    Importe = precio * (1 + (IVA / 100))
    assert Total(precio,IVA) == f"El coste final es {110.00000000000001} euros"