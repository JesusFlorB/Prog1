from src.ejercicio21 import invertir_frase

def test_frase_invertida():
    frase = "hola mundo"
    frase_invertida = frase[::-1]
    assert invertir_frase(frase,frase_invertida) == "odnum aloh"