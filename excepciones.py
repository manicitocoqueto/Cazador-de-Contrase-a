# excepciones.py

class LongitudInvalidaError(Exception):
    """Excepción para longitud de contraseña menor a 8 caracteres."""
    def __init__(self, mensaje="La longitud mínima permitida es de 8 caracteres."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class DatosNoNumericosError(Exception):
    """Excepción para cuando se ingresan datos no numéricos en la longitud."""
    def __init__(self, mensaje="Error: Debe ingresar un número entero válido."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ContrasenaInvalidaError(Exception):
    """Excepción para cuando la contraseña generada es incorrecta o inválida."""
    def __init__(self, mensaje="La contraseña generada es incorrecta y no cumple los requisitos."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)