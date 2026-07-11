# juego.py
import tkinter as tk
from tkinter import messagebox
from contrasena import Contrasena
from cofre import Cofre
from excepciones import LongitudInvalidaError, DatosNoNumericosError, ContrasenaInvalidaError

class JuegoCazador:
    """Clase JuegoCazador: administra el puntaje y controla el flujo mediante una interfaz gráfica (Tkinter)."""
    
    def __init__(self):
        self.puntaje_acumulado = 0
        self.ronda = 1
        
        # Configuración de la ventana principal
        self.root = tk.Tk()
        self.root.title("UNAD - Cazador de Contraseñas")
        self.root.geometry("550x500")
        self.root.resizable(False, False)
        
        self._crear_interfaz()

    def _crear_interfaz(self):
        """Dibuja los componentes de la interfaz gráfica."""
        # Encabezado Institucional
        lbl_unad = tk.Label(self.root, text="🏛️ UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA", font=("Arial", 11, "bold"))
        lbl_unad.pack(pady=5)
        
        lbl_datos = tk.Label(self.root, text="Curso: Programación (213023) | Estudiante: Verónica Valencia Cortez", font=("Arial", 9, "italic"))
        lbl_datos.pack(pady=2)
        
        # LÍNEA CORREGIDA: se cambió 'px' por 'padx'
        frame_linea = tk.Frame(self.root, height=2, bd=1, relief="groove")
        frame_linea.pack(fill="x", padx=10, pady=5)

        # Información de Estado (Ronda y Puntaje)
        self.lbl_ronda = tk.Label(self.root, text=f"--- RONDA {self.ronda} ---", font=("Arial", 12, "bold"), fg="blue")
        self.lbl_ronda.pack(pady=5)
        
        self.lbl_puntos = tk.Label(self.root, text=f"Puntaje acumulado: {self.puntaje_acumulado} puntos", font=("Arial", 11, "bold"))
        self.lbl_puntos.pack(pady=5)

        # Entrada de usuario
        lbl_instruccion = tk.Label(self.root, text="Defina la longitud de la contraseña (mínimo 8):", font=("Arial", 10))
        lbl_instruccion.pack(pady=10)
        
        self.txt_longitud = tk.Entry(self.root, font=("Arial", 11), width=10, justify="center")
        self.txt_longitud.pack(pady=5)

        # Botón de acción principal
        btn_generar = tk.Button(self.root, text="🕹️ Generar y Abrir Cofre", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", command=self.procesar_jugada)
        btn_generar.pack(pady=15)

        # Panel de Resultados
        self.lbl_pass_resultado = tk.Label(self.root, text="Contraseña generada: (Esperando...)", font=("Courier", 10, "bold"), fg="darkgreen")
        self.lbl_pass_resultado.pack(pady=10)
        
        self.lbl_cofre_resultado = tk.Label(self.root, text="Tipo de cofre obtenido: -", font=("Arial", 10, "bold"))
        self.lbl_cofre_resultado.pack(pady=5)

    def procesar_jugada(self):
        """Captura la entrada, valida las excepciones y actualiza la interfaz gráfica."""
        entrada_longitud = self.txt_longitud.get().strip()
        
        try:
            # 1. Excepción: Datos no numéricos
            if not entrada_longitud.isdigit():
                raise DatosNoNumericosError()
            
            longitud = int(entrada_longitud)
            
            # Instanciación y generación
            obj_contrasena = Contrasena(longitud)
            contrasena_generada = obj_contrasena.generar_contrasena()
            
            self.lbl_pass_resultado.config(text=f"Contraseña generada: {contrasena_generada}")
            
            # 2. Validación estricta
            if obj_contrasena.validar_contrasena():
                cofre_obtenido = Cofre(es_valida=True)
                self.puntaje_acumulado += cofre_obtenido.puntos
                self.lbl_cofre_resultado.config(text=f"Tipo de cofre obtenido: 🎉 {cofre_obtenido.tipo} (+{cofre_obtenido.puntos} pts)", fg="green")
            else:
                # 3. Excepción: Contraseña incorrecta
                raise ContrasenaInvalidaError()

        except (LongitudInvalidaError, DatosNoNumericosError) as error_formato:
            messagebox.showerror("⚠️ Excepción Detectada", str(error_formato))
            self._aplicar_cofre_maldito()
            
        except ContrasenaInvalidaError as error_pass:
            messagebox.showerror("❌ Excepción de Contraseña", str(error_pass))
            self._aplicar_cofre_maldito()

        # Actualizar marcadores y preparar siguiente ronda
        self.lbl_puntos.config(text=f"Puntaje acumulado: {self.puntaje_acumulado} puntos")
        self.txt_longitud.delete(0, tk.END)
        self.ronda += 1
        self.lbl_ronda.config(text=f"--- RONDA {self.ronda} ---")

    def _aplicar_cofre_maldito(self):
        """Lógica auxiliar para aplicar la penalización del cofre maldito."""
        cofre_maldito = Cofre(es_valida=False)
        self.puntaje_acumulado += cofre_maldito.puntos
        self.lbl_pass_resultado.config(text="Contraseña generada: ERROR", fg="red")
        self.lbl_cofre_resultado.config(text=f"Tipo de cofre obtenido: 💀 {cofre_maldito.tipo} ({cofre_maldito.puntos} pts)", fg="red")

    def iniciar_juego(self):
        """Lanza el ciclo principal de Tkinter para pintar la ventana."""
        self.root.mainloop()