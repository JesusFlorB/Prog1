from src.ejercicio4 import temperatura

def test_temperatura():
    Celsius = 35
    Fahrenheit = Celsius * 9/5 + 32
    assert temperatura(Fahrenheit) == f"La temperatura es {95.0} grados Fahrenheit"