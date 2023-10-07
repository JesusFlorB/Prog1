from src.ejercicio2 import coste_servicio

def test_costehora():
    horas = 7
    costehora = 5
    assert coste_servicio(horas,costehora) == "Tu sueldo diario es de 35 euros"