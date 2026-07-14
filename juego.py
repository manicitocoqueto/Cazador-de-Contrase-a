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
        self.root.geometry("580x520")
        self.root.configure(bg="#F4F6F9")  # Fondo gris azulado muy suave y limpio
        self.root.resizable(False, False)
        
        # Mostrar pantalla de inicio al inicializar
        self.mostrar_pantalla_inicio()

    def mostrar_pantalla_inicio(self):
        """Dibuja la pantalla de bienvenida con estilo plano institucional."""
        self._limpiar_ventana()
        
        # Panel superior decorativo (Azul UNAD)
        header_frame = tk.Frame(self.root, bg="#001F3F", height=100)
        header_frame.pack(fill="x", side="top")
        header_frame.pack_propagate(False)
        
        lbl_unad = tk.Label(header_frame, text="UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA", 
                            font=("Segoe UI", 12, "bold"), fg="#FFFFFF", bg="#001F3F")
        lbl_unad.pack(pady=15)
        
        lbl_sub = tk.Label(header_frame, text="UNAD - Escuela de Ciencias Básicas, Tecnología e Ingeniería", 
                           font=("Segoe UI", 9), fg="#F2B134", bg="#001F3F")
        lbl_sub.pack()

        # Datos del estudiante y curso
        info_frame = tk.Frame(self.root, bg="#FFFFFF", bd=1, relief="solid", highlightthickness=0)
        info_frame.pack(pady=25, padx=40, fill="x")
        
        lbl_datos = tk.Label(info_frame, 
                             text="Estudiante: Verónica Valencia Cortez\nCurso: Programación (213023_36)", 
                             font=("Segoe UI", 10, "bold"), fg="#333333", bg="#FFFFFF", pady=15)
        lbl_datos.pack()
        
        # Título del juego (Limpio, sin figuras raras)
        lbl_bienvenida = tk.Label(self.root, text="CAZADOR DE CONTRASEÑAS", 
                                  font=("Segoe UI", 16, "bold"), fg="#1F4E79", bg="#F4F6F9")
        lbl_bienvenida.pack(pady=10)
        
        # Botones Planos Modernos
        btn_iniciar = tk.Button(self.root, text="Iniciar Juego", font=("Segoe UI", 11, "bold"), 
                                bg="#2ECC71", fg="white", relief="flat", activebackground="#27AE60", 
                                activeforeground="white", width=20, height=2, cursor="hand2", command=self.comenzar_partida)
        btn_iniciar.pack(pady=8)
        
        btn_salir = tk.Button(self.root, text="Salir", font=("Segoe UI", 11, "bold"), 
                              bg="#E74C3C", fg="white", relief="flat", activebackground="#C0392B", 
                              activeforeground="white", width=20, height=2, cursor="hand2", command=self.root.quit)
        btn_salir.pack(pady=8)

    def comenzar_partida(self):
        """Cambia la pantalla de inicio por la interfaz activa del juego."""
        self._limpiar_ventana()
        self._crear_interfaz_juego()

    def _crear_interfaz_juego(self):
        """Dibuja los componentes del juego activo."""
        self.root.configure(bg="#FFFFFF")  # Fondo blanco para el juego activo
        
        # Encabezado superior minimalista
        top_bar = tk.Frame(self.root, bg="#001F3F", height=40)
        top_bar.pack(fill="x")
        top_bar.pack_propagate(False)
        
        lbl_est = tk.Label(top_bar, text="Verónica Valencia Cortez  |  Curso: 213023_36", 
                           font=("Segoe UI", 9, "bold"), fg="#FFFFFF", bg="#001F3F")
        lbl_est.pack(pady=10)

        # Información de Estado (Ronda y Puntaje)
        self.lbl_ronda = tk.Label(self.root, text=f"Ronda {self.ronda}", font=("Segoe UI", 14, "bold"), fg="#1F4E79", bg="#FFFFFF")
        self.lbl_ronda.pack(pady=15)
        
        self.lbl_puntos = tk.Label(self.root, text=f"Puntaje acumulado: {self.puntaje_acumulado} puntos", font=("Segoe UI", 11, "bold"), fg="#333333", bg="#FFFFFF")
        self.lbl_puntos.pack(pady=5)

        # Campo de Entrada
        lbl_instruccion = tk.Label(self.root, text="Defina la longitud de la contraseña (mínimo 8):", font=("Segoe UI", 10), fg="#555555", bg="#FFFFFF")
        lbl_instruccion.pack(pady=10)
        
        self.txt_longitud = tk.Entry(self.root, font=("Segoe UI", 12), width=12, justify="center", bd=1, relief="solid")
        self.txt_longitud.pack(pady=5)
        self.txt_longitud.focus()

        # Botón para generar (Estilo azul plano)
        btn_generar = tk.Button(self.root, text="Generar y Abrir Cofre", font=("Segoe UI", 10, "bold"), 
                                bg="#3498DB", fg="white", relief="flat", activebackground="#2980B9", 
                                activeforeground="white", width=22, height=2, cursor="hand2", command=self.procesar_jugada)
        btn_generar.pack(pady=15)

        # Panel de Resultados
        self.lbl_pass_resultado = tk.Label(self.root, text="Contraseña generada: (Esperando longitud...)", font=("Consolas", 10), fg="#7F8C8D", bg="#FFFFFF")
        self.lbl_pass_resultado.pack(pady=10)
        
        self.lbl_cofre_resultado = tk.Label(self.root, text="Resultado: -", font=("Segoe UI", 11, "bold"), fg="#333333", bg="#FFFFFF")
        self.lbl_cofre_resultado.pack(pady=5)
        
        # Botón para finalizar partida (Estilo morado plano)
        btn_finalizar = tk.Button(self.root, text="Finalizar y Mostrar Resumen", font=("Segoe UI", 10, "bold"), 
                                  bg="#9B59B6", fg="white", relief="flat", activebackground="#8E44AD", 
                                  activeforeground="white", width=25, height=2, cursor="hand2", command=self.mostrar_resumen_final)
        btn_finalizar.pack(pady=20)

    def procesar_jugada(self):
        entrada_longitud = self.txt_longitud.get().strip()
        
        try:
            if not entrada_longitud.isdigit():
                raise DatosNoNumericosError()
            
            longitud = int(entrada_longitud)
            obj_contrasena = Contrasena(longitud)
            contrasena_generada = obj_contrasena.generar_contrasena()
            
            self.lbl_pass_resultado.config(text=f"Contraseña generada: {contrasena_generada}", fg="#27AE60")
            
            if obj_contrasena.validar_contrasena():
                cofre_obtenido = Cofre(es_valida=True)
                self.puntaje_acumulado += cofre_obtenido.puntos
                self.total_cofres += 1
                
                if cofre_obtenido.tipo == "Común":
                    self.contador_comunes += 1
                elif cofre_obtenido.tipo == "Raro":
                    self.contador_raros += 1
                elif cofre_obtenido.tipo == "Épico":
                    self.contador_epicos += 1
                elif cofre_obtenido.tipo == "Legendario":
                    self.contador_legendarios += 1
                    
                self.lbl_cofre_resultado.config(text=f"Cofre Abierto: {cofre_obtenido.tipo} (+{cofre_obtenido.puntos} pts)", fg="#27AE60")
            else:
                raise ContrasenaInvalidaError()

        except (LongitudInvalidaError, DatosNoNumericosError) as error_formato:
            messagebox.showerror("Excepción Detectada", str(error_formato))
            self._aplicar_cofre_maldito()
            
        except ContrasenaInvalidaError as error_pass:
            messagebox.showerror("Error de Robustez", str(error_pass))
            self._aplicar_cofre_maldito()

        # Avanzar de ronda
        self.lbl_puntos.config(text=f"Puntaje acumulado: {self.puntaje_acumulado} puntos")
        self.txt_longitud.delete(0, tk.END)
        self.ronda += 1
        self.lbl_ronda.config(text=f"Ronda {self.ronda}")

    def _aplicar_cofre_maldito(self):
        cofre_maldito = Cofre(es_valida=False)
        self.puntaje_acumulado += cofre_maldito.puntos
        self.total_cofres += 1
        self.contador_malditos += 1
        self.lbl_pass_resultado.config(text="Contraseña generada: ERROR EN VALIDACIÓN", fg="#C0392B")
        self.lbl_cofre_resultado.config(text=f"Cofre Abierto: {cofre_maldito.tipo} ({cofre_maldito.puntos} pts)", fg="#C0392B")

    def mostrar_resumen_final(self):
        """Limpia la pantalla e imprime el reporte consolidado de cofres abiertos sin emojis rotos."""
        self._limpiar_ventana()
        self.root.configure(bg="#F4F6F9")
        
        lbl_titulo_resumen = tk.Label(self.root, text="RESUMEN DE PARTIDA", font=("Segoe UI", 15, "bold"), fg="#1F4E79", bg="#F4F6F9")
        lbl_titulo_resumen.pack(pady=20)
        
        # Cuadro de estadísticas limpio
        texto_resumen = (
            f" Puntaje Final Alcanzado: {self.puntaje_acumulado} pts\n"
            f" Rondas Jugadas: {self.ronda - 1}\n"
            f" Total de cofres abiertos: {self.total_cofres}\n"
            f" ----------------------------------------\n"
            f" * Cofres Comunes: {self.contador_comunes}\n"
            f" * Cofres Raros: {self.contador_raros}\n"
            f" * Cofres Épicos: {self.contador_epicos}\n"
            f" * Cofres Legendarios: {self.contador_legendarios}\n"
            f" * Cofres Malditos: {self.contador_malditos}"
        )
        
        lbl_reporte = tk.Label(self.root, text=texto_resumen, font=("Consolas", 11, "bold"), justify="left", 
                               relief="solid", bd=1, padx=25, pady=20, bg="#FFFFFF", fg="#2C3E50")
        lbl_reporte.pack(pady=15)
        
        # Botones de cierre
        btn_volver = tk.Button(self.root, text="Volver al Inicio", font=("Segoe UI", 10, "bold"), 
                                bg="#2ECC71", fg="white", relief="flat", width=18, height=2, cursor="hand2", command=self.reiniciar_todo)
        btn_volver.pack(pady=6)
        
        btn_salir_final = tk.Button(self.root, text="Salir del Programa", font=("Segoe UI", 10, "bold"), 
                                     bg="#E74C3C", fg="white", relief="flat", width=18, height=2, cursor="hand2", command=self.root.quit)
        btn_salir_final.pack(pady=6)

    def reiniciar_todo(self):
        self._limpiar_ventana()
        self.__init__()

    def _limpiar_ventana(self):
        for componente in self.root.winfo_children():
            componente.destroy()

    def iniciar_juego(self):
        self.root.mainloop()