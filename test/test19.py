from src.ejercicio19 import nombre_tiene_letras

def test_nombre_tiene_letras():
    nombre = "JESUS"
    num_letras = len(nombre)
    nombre_mayusculas = nombre.upper()
    assert nombre_tiene_letras(num_letras,nombre_mayusculas,nombre) == f"JESUS tiene 5 letras"