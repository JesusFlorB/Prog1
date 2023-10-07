from src.ejercicio3 import valores

def test_valores():
    ancho = 17
    alto = 12.0
    assert valores(ancho,alto) == f"El resultado 1 es {8.5}\nEl resultado 2 es {8}\nEl resultado 3 es {4.0}\nEl resultado 4 es {11}"