# contrasena.py
import random
import string
from excepciones import LongitudInvalidaError

class Contrasena:
    """Clase Contraseña: encargada de generar y validar contraseñas."""
    
    # Lista de caracteres especiales estipulada por la guía
    CARACTERES_ESPECIALES = list("¿¡?=)(/¨*+-%&$#!.")

    def __init__(self, longitud):
        if longitud < 8:
            raise LongitudInvalidaError()
        self.longitud = longitud
        self.contenido = ""

    def generar_contrasena(self):
        """Genera una contraseña completamente aleatoria sin caracteres repetidos."""
        mayusculas = string.ascii_uppercase
        minusculas = string.ascii_lowercase
        numeros = string.digits
        especiales = Contrasena.CARACTERES_ESPECIALES

        # Asegurar un carácter obligatorio de cada tipo exigido
        pool_obligatorio = [
            random.choice(mayusculas),
            random.choice(minusculas),
            random.choice(numeros),
            random.choice(especiales)
        ]

        # Consolidar caracteres disponibles en el universo excluyendo duplicados iniciales
        todos_disponibles = list(mayusculas + minusculas + numeros) + especiales
        for char in pool_obligatorio:
            if char in todos_disponibles:
                todos_disponibles.remove(char)

        # Completar los caracteres restantes solicitados por el usuario
        restantes_necesarios = self.longitud - len(pool_obligatorio)
        pool_restante = random.sample(todos_disponibles, restantes_necesarios)

        # Mezclar todo para que no exista orden predecible
        lista_final = pool_obligatorio + pool_restante
        random.shuffle(lista_final)

        self.contenido = "".join(lista_final)
        return self.contenido

    def validar_contrasena(self):
        """Verifica de forma estricta el cumplimiento de los requisitos."""
        if len(self.contenido) < 8:
            return False
        if len(self.contenido) != len(set(self.contenido)):
            return False

        tiene_mayuscula = any(c.isupper() for c in self.contenido)
        tiene_minuscula = any(c.islower() for c in self.contenido)
        tiene_numero = any(c.isdigit() for c in self.contenido)
        tiene_especial = any(c in Contrasena.CARACTERES_ESPECIALES for c in self.contenido)

        return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial