from src.ejercicio15 import ahorros

def test_ahorrros():
    tasa_interes = 0.04
    cantidad_inicial = 1000
    saldo_1_año = round(cantidad_inicial * (1 + tasa_interes), 2)
    saldo_2_años = round(saldo_1_año * (1 + tasa_interes), 2)
    saldo_3_años = round(saldo_2_años * (1 + tasa_interes), 2)
    assert ahorros(tasa_interes, cantidad_inicial) == f"Los ahorros despues de un año seran de {1040.0} euros. Despues de dos años seran {1081.6} euros y despues de tres años seran {1124.86} euros"