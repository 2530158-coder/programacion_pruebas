# Palindrome Checker 
while True:

    print("Inserta 'exit' si desea salir del programa")

    phrase = input("Inserta tu phrase")
    try:
        
        if phrase == "exit":
            break
        if phrase.strip().lower() == phrase.strip().lower()[::-1]:
            print("Es un palindromo")
            print(phrase)
        else:
            print("No es un palindromo")

    except ValueError:
        break

# Preguntas de rescate 

"""
    Diferencias entre listas y tuplas:

    Las listas son mutables(se pueden modificar)
    en cambio las tuplas son inmutables
    (no se pueden modificar).
    
    En uno podemos insertar enteros y en el otro solo puedes
    insertar strings.

    Usos:

    Tuplas: Formulas
    Listas: lisatas de objetos



    Diferencia entre un ciclo for y un ciclo while
    El ciclo for es un ciclo finito en el que tu asignas la cantidad 
    de veces que deseas se repita
    y el ciclo while es un ciclo infinito
    del cual no podras salir a menos que insertes un break
    en el codigo o definir una variable como salida.

    El for conviene mas usarlo cuando quieras que lo que haya 
    escrito en el programa se repita una cierta cantidad de veces

    El while conviene mas usarlo cuando quieres hacer 
    un codigo en el que el usuario tenga un numero 
    limitado de intentos para equivocarse en el programa o, 
    el caso contrario, aunque se equivoque al escribir algo
    en el programa, no lo saque, si no que lo devuelva 
    al inicio del programa, ejemplo, un programa para determinar si
    un año es bisiesto 
        
    Que ventajas tiene usar funciones?

    El programa se vera mas legible y ordenado
    las funciones tambien pueden indicarle que hacer al usuario
    o marcar cual es su error
 
"""