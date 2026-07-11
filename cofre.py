# cofre.py
import random

class Cofre:
    """Clase Cofre: Modula las recompensas obtenidas en el juego."""
    
    def __init__(self, es_valida):
        if es_valida:
            # Probabilidades: 40% Común, 30% Raro, 20% Épico, 10% Legendario
            opciones = ["Común", "Raro", "Épico", "Legendario"]
            pesos = [40, 30, 20, 10]
            self.tipo = random.choices(opciones, weights=pesos, k=1)[0]
            
            # Asignación de puntos según el tipo
            if self.tipo == "Común":
                self.puntos = 10
            elif self.tipo == "Raro":
                self.puntos = 25
            elif self.tipo == "Épico":
                self.puntos = 50
            else:  # Legendario
                self.puntos = 100
        else:
            self.tipo = "Maldito"
            self.puntos = -20