from src.ejercicio22 import frase_letra_modificada

def test_frase_letra_modificada():
    frase = "hola mundo"
    vocal = "o"
    frase_modificada = frase.replace(vocal,vocal.upper())
    assert frase_letra_modificada(frase,vocal,frase_modificada) == f"hOla mundO"