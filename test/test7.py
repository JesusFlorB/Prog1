from src.ejercicio7 import suma

def test_suma():
    numeroUNO = 3
    numeroDOS = 6
    numeroTRES = 9
    numerosSumados = numeroUNO + numeroDOS + numeroTRES
    assert suma(numeroUNO,numeroDOS,numeroTRES) == f"La suma de los tres numeros es {18}"