# contrasena.py
import random
import string
from excepciones import LongitudInvalidaError

class Contrasena:
    """Clase Contrasena: Encapsula los atributos y métodos para la creación de claves robustas."""
    
    def __init__(self, longitud):
        # Validación de la excepción de longitud en el constructor
        if longitud < 8:
            raise LongitudInvalidaError()
        self._longitud = longitud
        self._valor = ""

    # Métodos Getter y Setter (Encapsulamiento)
    @property
    def longitud(self):
        return self._longitud

    @property
    def valor(self):
        return self._valor

    def generar_contrasena(self):
        """Genera una contraseña aleatoria garantizando al menos un carácter de cada tipo obligatorio."""
        # 1. Asegurar la presencia de los requisitos mínimos
        letra_mayuscula = random.choice(string.ascii_uppercase)
        letra_minuscula = random.choice(string.ascii_lowercase)
        numero = random.choice(string.digits)
        caracter_especial = random.choice("!@#$%^&*()-_=+[]{}|;:,.<>?")
        
        recolectados = [letra_mayuscula, letra_minuscula, numero, caracter_especial]
        
        # 2. Completar los caracteres restantes
        todos_disponibles = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>?"
        restantes_necesarios = self._longitud - len(recolectados)
        
        # SOLUCIÓN: Usamos 'choices' (con reemplazo) para permitir longitudes mayores a la población de caracteres
        pool_restante = random.choices(todos_disponibles, k=restantes_necesarios)
        
        # Unir y mezclar
        lista_final = recolectados + pool_restante
        random.shuffle(lista_final)
        
        self._valor = "".join(lista_final)
        return self._valor

    def validar_contrasena(self):
        """Evalúa si la contraseña generada cumple de forma estricta con los 4 criterios de seguridad."""
        tiene_mayuscula = any(c.isupper() for c in self._valor)
        tiene_minuscula = any(c.islower() for c in self._valor)
        tiene_numero = any(c.isdigit() for c in self._valor)
        tiene_especial = any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?" for c in self._valor)
        
        return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial