from src.ejercicio1 import saludo
from src.ejercicio2 import coste_servicio
from src.ejercicio3 import valores
from src.ejercicio4 import temperatura
from src.ejercicio5 import Total
from src.ejercicio7 import suma
from src.ejercicio10 import resultadoOperacion
from src.ejercicio11 import sumaEnteros
from src.ejercicio12 import calculoIMC
from src.ejercicio13 import division
from src.ejercicio14 import pesoPaquete
from src.ejercicio15 import ahorros
from src.ejercicio16 import costePan
from src.ejercicio17 import imprimir_nombre_multiples_veces
from src.ejercicio19 import nombre_tiene_letras
from src.ejercicio20 import mostrar_telefono
from src.ejercicio21 import invertir_frase
from src.ejercicio22 import frase_letra_modificada
from src.ejercicio23 import cambiar_dominio_correo
from src.ejercicio24 import obtener_euros_y_centimos


#ejercicio1
def test_saludo():
    assert saludo("jesus") == "hola jesus"

#ejercicio2   
def test_costehora():
    horas = 7
    costehora = 5
    assert coste_servicio(horas,costehora) == "Tu sueldo diario es de 35 euros"

#ejercicio3    
def test_valores():
    ancho = 17
    alto = 12.0
    assert valores(ancho,alto) == f"El resultado 1 es {8.5}\nEl resultado 2 es {8}\nEl resultado 3 es {4.0}\nEl resultado 4 es {11}"
    
#ejercicio4
def test_temperatura():
    Celsius = 35
    Fahrenheit = Celsius * 9/5 + 32
    assert temperatura(Fahrenheit) == f"La temperatura es {95.0} grados Fahrenheit"
    
#ejercicio5
def test_Total():
    precio = 100
    IVA = 10
    Importe = precio * (1 + (IVA / 100))
    assert Total(precio,IVA) == f"El coste final es {110.00000000000001} euros"
    
#ejercicio7
def test_suma():
    numeroUNO = 3
    numeroDOS = 6
    numeroTRES = 9
    numerosSumados = numeroUNO + numeroDOS + numeroTRES
    assert suma(numeroUNO,numeroDOS,numeroTRES) == f"La suma de los tres numeros es {18}"
    
#ejercicio10
def test_operaciones():
    operando1 = 3
    operando2 = 2
    operando3 = 5
    operacion = (operando1 + operando2 / operando2 * operando3) ** operando2
    assert resultadoOperacion(operando1,operando2,operando3) == f"El resultado de la operacion es {64.0}"
    
#ejercicio11
def test_suma_enteros():
    n = 5
    suma = (n * (n + 1)) // 2
    assert sumaEnteros(n) == f"La suma de los enteros desde 1 hasta n es {15}"
    
#ejercicio12
def test_calculo_IMC():
    peso = 60.5
    estatura = 1.80
    imc = peso / (estatura**2)
    imc = round(imc, 2)
    assert calculoIMC(peso,estatura) == f"Tu indice de masa corporal es {18.67}"
    
#ejercicio13
def test_division():
    n = 4
    m = 2
    c = n // m
    r = n % m
    assert division(n,m,c,r) == f"La división de {4} entre {2} da un cociente {2} y un resto {0}."
    
#ejercicio14
def test_peso_muñecos():
    num_payasos = 50
    num_muñecas = 50
    peso_payaso = 112
    peso_muñeca = 75
    peso_total = (num_payasos * peso_payaso) + (num_muñecas * peso_muñeca)
    assert pesoPaquete(peso_payaso,peso_muñeca,num_payasos,num_muñecas) == f"El peso del paquete es {9350} gramos"
    
#ejercicio15
def test_ahorrros():
    tasa_interes = 0.04
    cantidad_inicial = 1000
    saldo_1_año = round(cantidad_inicial * (1 + tasa_interes), 2)
    saldo_2_años = round(saldo_1_año * (1 + tasa_interes), 2)
    saldo_3_años = round(saldo_2_años * (1 + tasa_interes), 2)
    assert ahorros(tasa_interes, cantidad_inicial) == f"Los ahorros despues de un año seran de {1040.0} euros. Despues de dos años seran {1081.6} euros y despues de tres años seran {1124.86} euros"
    
#ejercicio16
def test_barras_pan():
    barras_no_frescas_vendidas = 20
    precio_por_barra = 3.49
    descuento_no_fresca = 0.6
    costo_total_no_frescas = round(barras_no_frescas_vendidas * precio_por_barra * (1 - descuento_no_fresca))
    assert costePan(precio_por_barra,descuento_no_fresca,barras_no_frescas_vendidas) == f"El precio de una barra de pan es {3.49} euros, el descuento por no ser fresca es de {0.6} euros y el coste final de todas las barras de pan no frescas es de {28} euros"
    
#ejercicio17
def imprimir_nombre_multiples_veces(nombre, numero):
    for _ in range(numero):
        print(nombre)

def test_imprimir_nombre_multiples_veces(capsys):
    imprimir_nombre_multiples_veces('jesus', 3)
    captured = capsys.readouterr()
    assert captured.out == 'jesus\njesus\njesus\n'

#ejercicio19   
def test_nombre_tiene_letras():
    nombre = "JESUS"
    num_letras = len(nombre)
    nombre_mayusculas = nombre.upper()
    assert nombre_tiene_letras(num_letras,nombre_mayusculas,nombre) == f"JESUS tiene 5 letras"
    
#ejercicio20
def obtener_numero_sin_prefijo_y_extension(telefono):
    partes = telefono.split('-')
    numero = partes[1]
    return numero

def test_mostrar_telefono():
    telefono = f"+34-123456789-55"
    partes = telefono.split('-')
    numero = partes[1]
    resultado = obtener_numero_sin_prefijo_y_extension("+34-123456789-55")
    assert mostrar_telefono(telefono,partes,numero) == "123456789"

#ejercicio21    
def test_frase_invertida():
    frase = "hola mundo"
    frase_invertida = frase[::-1]
    assert invertir_frase(frase,frase_invertida) == "odnum aloh"
    
#ejercicio22
def test_frase_letra_modificada():
    frase = "hola mundo"
    vocal = "o"
    frase_modificada = frase.replace(vocal,vocal.upper())
    assert frase_letra_modificada(frase,vocal,frase_modificada) == f"hOla mundO"
    
#ejercicio23
def test_cambiar_dominio_correo():
    correo_original = "jesusflorbarrios@gmail.com"
    partes = correo_original.split('@')
    nombre = partes[0]
    nuevo_correo = nombre + '@ceu.es'
    nuevo_correo = cambiar_dominio_correo(correo_original)
    assert cambiar_dominio_correo(correo_original) == f"jesusflorbarrios@ceu.es"
    
#ejercicio24
def test_obtener_euros_y_centimos():
    euros, centimos = obtener_euros_y_centimos(15.75)
    assert euros == 15
    assert centimos == 75