from src.ejercicio12 import calculoIMC

def test_calculo_IMC():
    peso = 60.5
    estatura = 1.80
    imc = peso / (estatura**2)
    imc = round(imc, 2)
    assert calculoIMC(peso,estatura) == f"Tu indice de masa corporal es {18.67}"