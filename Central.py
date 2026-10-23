import random
import palabras
import ahorcado

palabra_secreta = random.choice(palabras.lista_palabras)

vidas = 6
letras_adivinadas = []

while vidas > 0:
    print("Vidas restantes: ", vidas)
    print(ahorcado.dibujos[vidas])

    palabra_adivinada = ""
    for i in palabra_secreta:
        if i in letras_adivinadas:
            palabra_adivinada += i
        else:
            palabra_adivinada += "_"

    print("Palabra: ", palabra_adivinada)  # probando
