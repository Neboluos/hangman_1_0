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
- [x] Implementar la lectura aleatoria de palabras desde `palabras.py`.
- [x] Enmascarar la palabra oculta con guiones bajos (`_`).
- [x] Validar la entrada del usuario (solo letras de la [A-Z], no repetir letras, no números).
- [x] Controlar el sistema de 6 vidas y restar en caso de error.
- [x] Hacer los ahorcados.
- [x] Importar y mostrar el ahorcado correspondiente desde `ahorcado.py` según las vidas restantes.

### Finalización y Flujo
- [ ] Mostrar mensaje de "Ganaste" o "Perdiste" (revelando la palabra).
- [ ] Implementar el menú final para reiniciar el juego o salir del programa.

### Por que escogi esas desiciones

1. Los ahorcados y las palabras los hice como una lista porque son más faciles de llamar al codigo principal
y porque puedo usar el import random en las palabras

2. Probe el random de la seleccion de palabras

3. Defini las vidas y las letras adivinadas para que el programa guarde las ingresadas por el usuario y sepa cuales han sido adivinadas

4. Inicie un while porque se pide que el programa se cierre cuando el usuario lo quiera

5. Defino palabras_adivinadas como vacio para que el programa vea si las letras de la palabra_secreta estan en ella, si no estan,
las convierte en un guion bajo _

6. Coloco .lower al final del input por si ingresa la letra en mayuscula la pase a minuscula y sea valida

7. Uso el comando .isalpha para verificar si lo ingresado es una letra, si no, le pide que ingrese otra vez una letra

8. Uso el continue al final de cada error ingresado por el usuario para que el codigo vuelva otra vez al input

9. Si la letra ingresada ya esta en la lista de letras_ingresadas le pide al usuario que use otra letra

10. Verifica que si la longitud del input es mayor a 1, osea mas de una letra, pide que ingrese solo una letra

11. Si la letra esta en la palabra secreta la agrega a la lista de letras_adivinadas

12. Si la letra no esta en la palabra secreta, le resta una vida, al restar la vida se cambia automaticamente el ahorcado

13. Al probar el codigo, el print para enseñar la pabalabra oculta mostraba todo el proceso de como el for busca letra por letra y lo convertia a: _ , entonces movi el print en la misma columna del for para que solo mostrara el resultado final de ese proceso

14. Al probar el codigo el ahorcado no mostraba la pierna ni el brazo izquierdo, porque el signo \ es como un salto de linea,
entonces se coloca r antes de la triple comillas para que el programa lo vea como un signo y ya, y no por lo que debe hacer

#Del 6 hasta el 14 se me olvido que por cada solucion hacer un push, pero si lo probe varias veces, mala mia..