"""Escribe un programa para pedirle al usuario las horas de trabajo 
y el precio por hora y calcule el importe total del servicio."""

def coste_servicio(horas,costehora): 
    SueldoDiario = horas * costehora
    return f"Tu sueldo diario es de {SueldoDiario} euros"
if __name__=="__main__":

    horas = int(input("¿Cuantas horas trabajas al dia?: "))
    costehora = int(input("¿Cual es el coste de una hora de trabajo?: "))

    print (coste_servicio(horas,costehora))