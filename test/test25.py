from src.ejercicio25 import obtener_fecha_nacimiento
from io import StringIO
import sys

def test_obtener_fecha_nacimiento(monkeypatch):
    # Simulamos la entrada del usuario para la fecha "01/12/2000"
    monkeypatch.setattr('sys.stdin', StringIO('20/12/1993\n'))
    dia, mes, año = obtener_fecha_nacimiento()
    assert (dia, mes, año) == ("20", "12", "1993")