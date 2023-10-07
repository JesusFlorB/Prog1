from src.ejercicio24 import obtener_euros_y_centimos

def test_obtener_euros_y_centimos():
    euros, centimos = obtener_euros_y_centimos(15.75)
    assert euros == 15
    assert centimos == 75