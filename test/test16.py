from src.ejercicio16 import costePan

def test_barras_pan():
    barras_no_frescas_vendidas = 20
    precio_por_barra = 3.49
    descuento_no_fresca = 0.6
    costo_total_no_frescas = round(barras_no_frescas_vendidas * precio_por_barra * (1 - descuento_no_fresca))
    assert costePan(precio_por_barra,descuento_no_fresca,barras_no_frescas_vendidas) == f"El precio de una barra de pan es {3.49} euros, el descuento por no ser fresca es de {0.6} euros y el coste final de todas las barras de pan no frescas es de {28} euros"