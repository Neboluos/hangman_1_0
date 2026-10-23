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

    print("Palabra: ", palabra_adivinada)

    adivinada = input("Adivina una letra(A-Z): ").lower()
    if adivinada.isalpha() == False:
        print("Por favor ingrese solo letras")
        continue
    elif adivinada in letras_adivinadas:
        print("Ya ingresaste esta letra, intenta con otra")
        continue
    elif len(adivinada) > 1:
        print("Por favor ingrese solo una letra")
        continue
    else:
        letras_adivinadas.append(adivinada)
        if adivinada not in palabra_secreta:
            vidas -= 1
            print("Letra incorrecta")
        else:
            print("Letra correcta")
         

