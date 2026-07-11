# 🏛️ Universidad Nacional Abierta y a Distancia (UNAD)
## Curso: Programación - Código: 213023_36
### Fase 5 - Entrega Proyecto de Software: Cazador de Contraseñas (Versión Tkinter)

**Estudiante:** Verónica Valencia Cortez  
**Entorno de Desarrollo:** Python 3.13 / Visual Studio Code  
**Interfaz Gráfica:** Tkinter (Biblioteca Nativa de Python)

---

## 🕹️ Descripción del Proyecto
El **Cazador de Contraseñas** es una aplicación de escritorio interactiva desarrollada bajo el paradigma de **Programación Orientada a Objetos (POO)**. El objetivo del juego es acumular la mayor cantidad de puntos abriendo cofres de recompensas, los cuales se desbloquean únicamente generando contraseñas seguras y válidas que cumplan con los criterios del sistema.

### 🧩 Arquitectura del Software (Clases y Estructura)
El sistema está dividido modularmente para garantizar el cumplimiento de los pilares de la POO:
1. **`Contrasena` (`contrasena.py`):** Encargada de encapsular la lógica de generación aleatoria (letras, números, caracteres especiales) y validación estricta de robustez.
2. **`Cofre` (`cofre.py`):** Modula los tipos de cofres disponibles (Común, Épico, Legendario, Maldito) y asigna las puntuaciones correspondientes de manera dinámica.
3. **`JuegoCazador` (`juego.py`):** Controla el flujo principal del juego, administra las rondas, los puntajes acumulados y construye la interfaz gráfica de usuario (GUI).
4. **`Manejador de Excepciones` (`excepciones.py`):** Define los errores personalizados del sistema para evitar cierres inesperados.
5. **`Punto de Entrada` (`main.py`):** Archivo principal encargado de inicializar y arrancar la aplicación.

---

## ⚠️ Control de Excepciones Personalizadas
El programa implementa un control de errores robusto mediante ventanas emergentes de alerta (`messagebox.showerror`), capturando las siguientes excepciones de manera específica:

* **`DatosNoNumericosError`:** Se dispara si el usuario ingresa letras, símbolos o deja vacío el campo de longitud.
* **`LongitudInvalidaError`:** Se activa si el valor numérico ingresado es inferior a 8 caracteres.
* **`ContrasenaInvalidaError`:** Se genera de manera interna si la clave creada no supera los filtros obligatorios de seguridad.

*Nota: Al dispararse cualquier excepción, el sistema penaliza al jugador otorgándole un **Cofre Maldito** que resta puntos.*

---

## 🚀 Instrucciones de Ejecución

1. Asegúrate de tener instalado **Python 3.x** en tu sistema.
2. Descarga o clona este repositorio en tu máquina local.
3. Abre una terminal dentro de la carpeta del proyecto y ejecuta el archivo principal:

```bash
python main.py