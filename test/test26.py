from src.ejercicio26 import mostrar_productos
from io import StringIO
import sys

def test_mostrar_productos(capsys):
    # Simulamos la entrada del usuario para los productos "Manzana,Pera,Naranja"
    productos = "Manzana,Pera,Naranja"
    mostrar_productos(productos)
    captured = capsys.readouterr()
    assert captured.out == "Manzana\nPera\nNaranja\n"