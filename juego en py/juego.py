import random


def presentacion():
        print("Hola Bienvenido")
        print("Estas por jugar Hi-Lo")
        respuesta = input("Sabes jugar?(SI/NO) ")
        if respuesta == "si":
                print(" ")
                print("Muy bien empezemos!")
        else:
                print(" ")
                print("En Hi-Lo se trata de adivinar si la siguiente carta será más alta o más baja que la anterior(Entre el 1 y el 10). Si adivinas bien, ganas, si no, pierdes. ")


def juego (contador):
        perdi = False
        print(" ")
        print("-------------------------------")
        print("numero Inicial")
        num1 = random.randint(1, 10)
        print(num1)
        while perdi == False:
            decicion = input("Mayor o Menor?(HI/LO) ")
            if decicion == "hi":
                   num2 = random.randint(1, 10)
                   print(num2)
                   if num2 >= num1:
                         contador = contador + 1
                         perdi = False
                   else:
                         perdi = True 
            elif decicion == "lo":
                  num2 = random.randint(1, 10)
                  print(num2)
                  if num2 <= num1:
                        contador = contador + 1
                        perdi = False
                  else:
                        perdi = True
            num1 = num2
            print(f"Puntuacion :{contador}")
        return contador

def iniciar_juego(contador,nom):
        presentacion()
        nom = input("Cual es tu Nombre? ")
        contador = juego(contador)
        return nom, contador
        




#Programa principal
contador = 0
nom = ""
nom, contador = iniciar_juego(contador,nom)
print("-------------------------------")
print(f"El jugador, {nom}, hizo {contador} puntos!")
print("-------------------------------")