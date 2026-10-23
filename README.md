# Juego del Ahorcado v1.0

### Datos del Estudiante
* **Nombre:** Juan Diego Tabarquino Valera
* **Correo:** juan.tabarquino@utp.edu.co

> [!NOTE]
> ### Instrucciones de Ejecución
> Para ejecutar este programa, asegúrate de tener Python instalado y corre el siguiente comando en tu consola:
> ```bash
> python Central.py
> ```

## Lista de Requerimientos y Tareas

### Configuración Inicial
- [x] Diseñar la estructura de archivos (`Central.py`, `palabras.py`, `ahorcado.py`).
- [x] Configurar el repositorio de Git y enlace a GitHub.

### Lógica del Juego
- [x] Predefinir algunas palabras.
- [ ] Implementar la lectura aleatoria de palabras desde `palabras.py`.
- [ ] Enmascarar la palabra oculta con guiones bajos (`_`).
- [ ] Validar la entrada del usuario (solo letras de la [A-Z], no repetir letras, no números).
- [ ] Controlar el sistema de 6 vidas y restar en caso de error.
- [x] Hacer los ahorcados.
- [ ] Importar y mostrar el ahorcado correspondiente desde `ahorcado.py` según las vidas restantes.

### Finalización y Flujo
- [ ] Mostrar mensaje de "Ganaste" o "Perdiste" (revelando la palabra).
- [ ] Implementar el menú final para reiniciar el juego o salir del programa.

### Por que escogi esas desiciones

1. Los ahorcados y las palabras los hice como una lista porque son más faciles de llamar al codigo principal
- y porque puedo usar el import random en las palabras
