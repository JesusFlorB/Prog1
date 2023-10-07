from src.ejercicio13 import division

def test_division():
    n = 4
    m = 2
    c = n // m
    r = n % m
    assert division(n,m,c,r) == f"La división de {4} entre {2} da un cociente {2} y un resto {0}."