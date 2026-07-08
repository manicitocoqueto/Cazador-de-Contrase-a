## main.py
# Archivo fuente principal que sirve como punto de entrada de la aplicación.

from juego import JuegoCazador

if __name__ == "__main__":
    # Instanciamos la clase principal que controla el flujo del juego
    cazador_juego = JuegoCazador()
    
    # Iniciamos la interfaz interactiva en la terminal
    cazador_juego.iniciar_juego()