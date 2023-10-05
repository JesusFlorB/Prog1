"""Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos 
en el último pedido y calcule el peso total del paquete que será enviado."""

def pesoPaquete(peso_payaso,peso_muñeca,num_payasos,num_muñecas):
    peso_total = (num_payasos * peso_payaso) + (num_muñecas * peso_muñeca)
    return f"El peso del paquete es {peso_total} gramos"

if __name__=="__main__":

    peso_payaso = 112  # en gramos
    peso_muñeca = 75   # en gramos
    num_payasos = int(input("Introduce el número de payasos vendidos: "))
    num_muñecas = int(input("Introduce el número de muñecas vendidas: "))
    peso_total = (num_payasos * peso_payaso) + (num_muñecas * peso_muñeca)
    print (pesoPaquete(peso_payaso,peso_muñeca,num_payasos,num_muñecas))