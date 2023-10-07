from src.ejercicio9 import solicitar_numero, calcular_suma
from io import StringIO
import sys

def test_solicitar_numero(monkeypatch):
    # Simulamos la entrada del usuario para el número 5.0
    monkeypatch.setattr('sys.stdin', StringIO('5.0\n'))
    resultado = solicitar_numero()
    assert resultado == 5.0

def test_calcular_suma(monkeypatch):
    # Simulamos la entrada del usuario para los números 1.0, 2.0, 3.0
    monkeypatch.setattr('sys.stdin', StringIO('1.0\n2.0\n3.0\n'))
    resultado = calcular_suma()
    assert resultado == 6.0