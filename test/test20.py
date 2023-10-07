from src.ejercicio20 import mostrar_telefono

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