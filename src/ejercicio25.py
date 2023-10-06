"""Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa 
y muestra por pantalla, el día, el mes y el año. 
Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter."""

def obtener_fecha_nacimiento():
    return dia, mes, año

if __name__=="__main__":

    fecha = input("Por favor, ingresa tu fecha de nacimiento (dd/mm/aaaa): ")
    partes = fecha.split('/') #separar los datos segun el argumento (/)
    dia = partes[0].zfill(2)  #rellenar con cero si es un solo carácter
    mes = partes[1].zfill(2)  #rellenar con cero si es un solo carácter
    año = partes[2]

#pedir la fecha de nacimiento
dia_nac, mes_nac, año_nac = obtener_fecha_nacimiento()

print(f"Día: {dia_nac}")
print(f"Mes: {mes_nac}")
print(f"Año: {año_nac}")