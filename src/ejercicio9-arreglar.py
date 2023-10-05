"""¿Es posible escribir el programa del ejercicio 1.7 sin usar variables? Inténtalo."""


while 1: 
    try:
        #lista vacia para guardar los numeros que ingrese el usuario
        num = []
        #ciclo for para capturar los numeros
        for i in range(3):
            #pedir al usuario ingresar los numeros
            numeros = int(input("Por favor introduce tres numeros: ")) 
            #guardar cada numero en la lista, finalizar programa y mostrar resultado
            num.append(numeros)
        sumaNumeros = sum(num)
        print(sumaNumeros)
        exit()
    #enviar alerta cuando el usuario introduzca un valor incorrecto
    except ValueError:
        print("ERROR. Introduzca un numero de tipo entero")