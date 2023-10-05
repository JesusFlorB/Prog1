"""Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado 
y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%)."""

def calcular_iva(importe_final, porcentaje_iva):
    iva_pagado = (porcentaje_iva / 100) * importe_final
    return iva_pagado

def calcular_importe_sin_iva(importe_final, iva_pagado):
    importe_sin_iva = importe_final - iva_pagado
    return importe_sin_iva

def main():
    importe_final = float(input("Ingrese el importe final del artículo: "))
    porcentaje_iva = 10

    iva_pagado = calcular_iva(importe_final, porcentaje_iva)
    importe_sin_iva = calcular_importe_sin_iva(importe_final, iva_pagado)

    print(f"IVA pagado: {iva_pagado} euros")
    print(f"Importe sin IVA: {importe_sin_iva} euros")

if __name__ == "__main__":
    main()