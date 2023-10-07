from src.ejercicio10 import resultadoOperacion

def test_operaciones():
    operando1 = 3
    operando2 = 2
    operando3 = 5
    operacion = (operando1 + operando2 / operando2 * operando3) ** operando2
    assert resultadoOperacion(operando1,operando2,operando3) == f"El resultado de la operacion es {64.0}"