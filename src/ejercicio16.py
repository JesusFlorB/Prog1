"""Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), 
el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas."""

def costePan(precio_por_barra,descuento_no_fresca,barras_no_frescas_vendidas):
    costo_total_no_frescas = round(barras_no_frescas_vendidas * precio_por_barra * (1 - descuento_no_fresca))
    return f"El precio de una barra de pan es {precio_por_barra} euros, el descuento por no ser fresca es de {descuento_no_fresca} euros y el coste final de todas las barras de pan no frescas es de {costo_total_no_frescas} euros"
    
if __name__=="__main__":
    
    precio_por_barra = 3.49 # en euros
    descuento_no_fresca = 0.6  # 60%
    barras_no_frescas_vendidas = int(input("Introduce el número de barras no frescas vendidas: "))
    print (costePan(precio_por_barra,descuento_no_fresca,barras_no_frescas_vendidas))