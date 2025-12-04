"""
    Docstring for understanding_while module

    Utilizamos el while loop para 
    ejecutar un bloque de código repetidamente
    mientras una condición sea verdadera.

    Estrucutura basica de while loop en Python:

        while condicion:
        # Bloque de codigo a ejecutar


"""
# Ejemplo basico de while loop
# Verificar si un numero esta en un
# rango especifico (10 y entre 20)

while True: # while loop infinito
    try:

        number = int(input("Ingrese un menor numero entre 10 y 20: "))

        if number < 20 and number > 10:
            print(f"Felicidades! {number} esta en el rango especifico.")
            break
        else:
            print(f"lo siento {number} no esta en el rango especifico.")

    except ValueError:
        print("Por favor ingrese un numero valido.")
    except KeyboardInterrupt: # Ctrl + C para terminar el programa
        print("\n Programa terminado por el ususario.")
        break

while True: 
    try:
        number_string = input("Ingrese un numero entero entre 10 y 20")

        if number_string.isdigits():
            number = int(number_string)
            