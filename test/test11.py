from src.ejercicio11 import sumaEnteros

def test_suma_enteros():
    n = 5
    suma = (n * (n + 1)) // 2
    assert sumaEnteros(n) == f"La suma de los enteros desde 1 hasta n es {15}"