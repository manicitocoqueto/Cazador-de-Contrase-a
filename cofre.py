# cofre.py
import random

class Cofre:
    """Clase Cofre: representa los cofres que se abren dependiendo de la calidad."""
    
    def __init__(self, es_valida):
        self.es_valida = es_valida
        self.tipo, self.puntos = self._asignar_premio()

    def _asignar_premio(self):
        """Asigna cofres positivos si es válida o cofre maldito si es inválida."""
        if not self.es_valida:
            return "Maldito", -20
        else:
            opciones = [
                ("Común", 10),
                ("Raro", 25),
                ("Legendario", 50)
            ]
            return random.choice(opciones)