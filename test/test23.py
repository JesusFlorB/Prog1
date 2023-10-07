from src.ejercicio23 import cambiar_dominio_correo

def test_cambiar_dominio_correo():
    correo_original = "jesusflorbarrios@gmail.com"
    partes = correo_original.split('@')
    nombre = partes[0]
    nuevo_correo = nombre + '@ceu.es'
    nuevo_correo = cambiar_dominio_correo(correo_original)
    assert cambiar_dominio_correo(correo_original) == f"jesusflorbarrios@ceu.es"