from src.ejercicio8 import obtener_tres_numeros, calcular_suma
from io import StringIO
import sys

def test_obtener_tres_numeros(monkeypatch):
    #simulamos la entrada del usuario para los números 1, 2 y 3
    monkeypatch.setattr('sys.stdin', StringIO('1\n2\n3\n'))
    resultado = obtener_tres_numeros()
    assert resultado == [1, 2, 3]

def test_calcular_suma():
    numeros = [1, 2, 3]
    resultado = calcular_suma(numeros)
    assert resultado == 6
