import random
import palabras
import ahorcado

while True:

    palabra_secreta = random.choice(palabras.lista_palabras)
    vidas = 6
    letras_adivinadas = []

    while vidas > 0:

        print(ahorcado.dibujos[vidas])
        print("Vidas restantes: ", vidas)


        palabra_adivinada = ""
        for i in palabra_secreta:
          if i in letras_adivinadas:
            palabra_adivinada += i
          else:
            palabra_adivinada += "_"

        print("Palabra: ", palabra_adivinada)
        
        if not "_" in palabra_adivinada:
            print("Felicidades, adivinaste la palabra: ", palabra_secreta)
            opcion = input("Presiona 1 si quieres volver a jugar, o cualquier otra tecla para salir: ")
            if opcion == "1":
                break
            else:
                exit()



        adivinada = input("Adivina una letra(A-Z): ").lower()
        if len(adivinada) > 1:
           print("Por favor ingrese solo una letra")
           continue
        elif adivinada.isalpha() == False:
           print("Por favor ingrese solo letras")
           continue
        elif adivinada in letras_adivinadas:
           print("Ya ingresaste esta letra, intenta con otra")
           continue
        else:
          letras_adivinadas.append(adivinada)
          if adivinada not in palabra_secreta:
            vidas -= 1
            print("Letra incorrecta")
          else:
            print("Letra correcta")


    if vidas == 0:
        print(ahorcado.dibujos[vidas])
        print("Vidas restantes: ", vidas)
        print("Perdiste, la palabra era: ", palabra_secreta)
        opcion = input("Presiona 1 si quieres volver a jugar, o cualquier otra tecla para salir: ")
        if opcion == "1":
            continue
        else:
            break


