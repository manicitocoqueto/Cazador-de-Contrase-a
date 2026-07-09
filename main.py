# ==============================================================================
# 🏛️ UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA (UNAD)
# Escuela de Ciencias Básicas, Tecnología e Ingeniería (ECBTI)
# Curso: Programación (Código: 213023)

# Estudiante: Verónica Valencia Cortez
# Actividad: Fase 5 - Entrega Proyecto de Software
# Proyecto: Juego Interactivo "Cazador de Contraseñas"
# Fecha: Julio de 2026
# ==============================================================================

# main.py
# Archivo fuente principal que sirve como punto de entrada de la aplicación.

from juego import JuegoCazador

if __name__ == "__main__":
    # Instanciamos la clase principal que controla el flujo del juego
    cazador_juego = JuegoCazador()
    
    # Iniciamos la interfaz interactiva en la terminal
    cazador_juego.iniciar_juego()