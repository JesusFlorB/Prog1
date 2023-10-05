"""Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
Redondear cada cantidad a dos decimales."""

def ahorros(tasa_interes,cantidad_inicial):
    saldo_1_año = round(cantidad_inicial * (1 + tasa_interes), 2)
    saldo_2_años = round(saldo_1_año * (1 + tasa_interes), 2)
    saldo_3_años = round(saldo_2_años * (1 + tasa_interes), 2)
    return f"Los ahorros despues de un año seran de {saldo_1_año} euros. Despues de dos años seran {saldo_2_años} euros y despues de tres años seran {saldo_3_años} euros"

if __name__=="__main__":
    
    tasa_interes = 0.04
    cantidad_inicial = float(input("Introduce la cantidad de dinero depositada en la cuenta de ahorros: "))
    print (ahorros(tasa_interes,cantidad_inicial))