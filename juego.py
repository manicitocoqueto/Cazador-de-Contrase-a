# juego.py
import tkinter as tk
from tkinter import messagebox
from contrasena import Contrasena
from cofre import Cofre
from excepciones import LongitudInvalidaError, DatosNoNumericosError, ContrasenaInvalidaError

class JuegoCazador:
    def __init__(self):
        # Variables de control del juego
        self.puntaje_acumulado = 0
        self.ronda = 1
        
        # Contadores para el resumen final
        self.total_cofres = 0
        self.contador_comunes = 0
        self.contador_raros = 0
        self.contador_epicos = 0
        self.contador_legendarios = 0
        self.contador_malditos = 0
        
        # Ventana Principal
        self.root = tk.Tk()
        self.root.title("UNAD - Cazador de Contraseñas")
        self.root.geometry("550x500")
        self.root.resizable(False, False)
        
        # Mostrar pantalla de inicio al inicializar
        self.mostrar_pantalla_inicio()

    def mostrar_pantalla_inicio(self):
        """Dibuja la pantalla de bienvenida con los botones de Inicio y Salida."""
        self._limpiar_ventana()
        
        # Encabezado Institucional
        lbl_unad = tk.Label(self.root, text="🏛️ UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA", font=("Arial", 12, "bold"))
        lbl_unad.pack(pady=20)
        
        lbl_datos = tk.Label(self.root, text="Curso: Programación (213023)\nEstudiante: Verónica Valencia Cortez", font=("Arial", 10, "italic"))
        lbl_datos.pack(pady=10)
        
        lbl_bienvenida = tk.Label(self.root, text="🎮 ¡BIENVENIDA AL CAZADOR DE CONTRASEÑAS! 🎮", font=("Arial", 13, "bold"), fg="darkblue")
        lbl_bienvenida.pack(pady=30)
        
        # Botón para iniciar el juego
        btn_iniciar = tk.Button(self.root, text="🚀 Iniciar Juego", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", width=18, height=2, command=self.comenzar_partida)
        btn_iniciar.pack(pady=10)
        
        # Botón para salir de la aplicación
        btn_salir = tk.Button(self.root, text="❌ Salir", font=("Arial", 11, "bold"), bg="#f44336", fg="white", width=18, height=2, command=self.root.quit)
        btn_salir.pack(pady=10)

    def comenzar_partida(self):
        """Cambia la pantalla de inicio por la interfaz activa del juego."""
        self._limpiar_ventana()
        self._crear_interfaz_juego()

    def _crear_interfaz_juego(self):
        """Dibuja los componentes para jugar las rondas."""
        # Datos fijos arriba
        lbl_datos = tk.Label(self.root, text="Estudiante: Verónica Valencia Cortez", font=("Arial", 9, "italic"))
        lbl_datos.pack(pady=5)

        # Información de Estado
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
        btn_generar = tk.Button(self.root, text="🕹️ Generar y Abrir Cofre", font=("Arial", 10, "bold"), bg="#2196F3", fg="white", command=self.procesar_jugada)
        btn_generar.pack(pady=10)

        # Panel de Resultados de la ronda
        self.lbl_pass_resultado = tk.Label(self.root, text="Contraseña generada: (Esperando...)", font=("Courier", 10, "bold"), fg="darkgreen")
        self.lbl_pass_resultado.pack(pady=10)
        
        self.lbl_cofre_resultado = tk.Label(self.root, text="Tipo de cofre obtenido: -", font=("Arial", 10, "bold"))
        self.lbl_cofre_resultado.pack(pady=5)
        
        # Botón obligatorio para finalizar y ver estadísticas totales
        btn_finalizar = tk.Button(self.root, text="📊 Finalizar y Mostrar Resumen", font=("Arial", 10, "bold"), bg="#9C27B0", fg="white", command=self.mostrar_resumen_final)
        btn_finalizar.pack(pady=25)

    def procesar_jugada(self):
        entrada_longitud = self.txt_longitud.get().strip()
        
        try:
            if not entrada_longitud.isdigit():
                raise DatosNoNumericosError()
            
            longitud = int(entrada_longitud)
            obj_contrasena = Contrasena(longitud)
            contrasena_generada = obj_contrasena.generar_contrasena()
            
            self.lbl_pass_resultado.config(text=f"Contraseña generada: {contrasena_generada}")
            
            if obj_contrasena.validar_contrasena():
                cofre_obtenido = Cofre(es_valida=True)
                self.puntaje_acumulado += cofre_obtenido.puntos
                self.total_cofres += 1
                
                # Clasificar el tipo de cofre abierto
                if cofre_obtenido.tipo == "Común":
                    self.contador_comunes += 1
                elif cofre_obtenido.tipo == "Raro":
                    self.contador_raros += 1
                elif cofre_obtenido.tipo == "Épico":
                    self.contador_epicos += 1
                elif cofre_obtenido.tipo == "Legendario":
                    self.contador_legendarios += 1
                    
                self.lbl_cofre_resultado.config(text=f"Tipo de cofre obtenido: 🎉 {cofre_obtenido.tipo} (+{cofre_obtenido.puntos} pts)", fg="green")
            else:
                raise ContrasenaInvalidaError()

        except (LongitudInvalidaError, DatosNoNumericosError) as error_formato:
            messagebox.showerror("⚠️ Excepción Detectada", str(error_formato))
            self._aplicar_cofre_maldito()
            
        except ContrasenaInvalidaError as error_pass:
            messagebox.showerror("❌ Excepción de Contraseña", str(error_pass))
            self._aplicar_cofre_maldito()

        # Avanzar de ronda
        self.lbl_puntos.config(text=f"Puntaje acumulado: {self.puntaje_acumulado} puntos")
        self.txt_longitud.delete(0, tk.END)
        self.ronda += 1
        self.lbl_ronda.config(text=f"--- RONDA {self.ronda} ---")

    def _aplicar_cofre_maldito(self):
        cofre_maldito = Cofre(es_valida=False)
        self.puntaje_acumulado += cofre_maldito.puntos
        self.total_cofres += 1
        self.contador_malditos += 1
        self.lbl_pass_resultado.config(text="Contraseña generada: ERROR", fg="red")
        self.lbl_cofre_resultado.config(text=f"Tipo de cofre obtenido: 💀 {cofre_maldito.tipo} ({cofre_maldito.puntos} pts)", fg="red")

    def mostrar_resumen_final(self):
        """Limpia la pantalla e imprime el reporte consolidado de cofres abiertos."""
        self._limpiar_ventana()
        
        lbl_titulo_resumen = tk.Label(self.root, text="📊 RESUMEN FINAL DE LA PARTIDA 📊", font=("Arial", 14, "bold"), fg="purple")
        lbl_titulo_resumen.pack(pady=20)
        
        # Cuadro de estadísticas estructurado
        texto_resumen = (
            f"Puntaje Final Alcanzado: {self.puntaje_acumulado} pts\n"
            f"Rondas Jugadas: {self.ronda - 1}\n\n"
            f"📦 Total de cofres abiertos: {self.total_cofres}\n"
            f"----------------------------------------\n"
            f"🟢 Cofres Comunes: {self.contador_comunes}\n"
            f"🔵 Cofres Raros: {self.contador_raros}\n"
            f"🟠 Cofres Épicos: {self.contador_epicos}\n"
            f"👑 Cofres Legendarios: {self.contador_legendarios}\n"
            f"💀 Cofres Malditos: {self.contador_malditos}"
        )
        
        lbl_reporte = tk.Label(self.root, text=texto_resumen, font=("Courier", 11, "bold"), justify="left", relief="solid", bd=1, padx=20, pady=20, bg="#FAFAFA")
        lbl_reporte.pack(pady=15)
        
        # Botón para volver a jugar o salir definitivamente
        btn_volver = tk.Button(self.root, text="🔄 Volver al Inicio", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", width=15, command=self.reiniciar_todo)
        btn_volver.pack(pady=5)
        
        btn_salir_final = tk.Button(self.root, text="🚪 Salir del Programa", font=("Arial", 10, "bold"), bg="#f44336", fg="white", width=15, command=self.root.quit)
        btn_salir_final.pack(pady=5)

    def reiniciar_todo(self):
        """Resetea las variables globales para permitir una nueva partida limpia."""
        self.__init__()

    def _limpiar_ventana(self):
        """Elimina todos los widgets activos en la pantalla actual."""
        for componente in self.root.winfo_children():
            componente.destroy()

    def iniciar_juego(self):
        self.root.mainloop()