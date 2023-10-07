from src.ejercicio17 import imprimir_nombre_multiples_veces

def imprimir_nombre_multiples_veces(nombre, numero):
    for _ in range(numero):
        print(nombre)
        
def test_imprimir_nombre_multiples_veces(capsys):
    imprimir_nombre_multiples_veces('jesus', 3)
    captured = capsys.readouterr()
    assert captured.out == 'jesus\njesus\njesus\n'