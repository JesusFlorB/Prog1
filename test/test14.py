from src.ejercicio14 import pesoPaquete

def test_peso_muñecos():
    num_payasos = 50
    num_muñecas = 50
    peso_payaso = 112
    peso_muñeca = 75
    peso_total = (num_payasos * peso_payaso) + (num_muñecas * peso_muñeca)
    assert pesoPaquete(peso_payaso,peso_muñeca,num_payasos,num_muñecas) == f"El peso del paquete es {9350} gramos"