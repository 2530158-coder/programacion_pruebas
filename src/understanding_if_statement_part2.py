"""
    Vamos a realizar un programa que pregunte 
    al usuario por su edad y muestre por pantalla
    si es mayor de edad o no.

"""

try:
    age = int(input("Por favor, introduce tu edad: "))



    if age >= 18:
        print("Eres mayor de edad.")
    elif age <18:
        print("Eres menor de edad.")

except:

    print("Tuviste un error al escribir tu edad. Por favor, introduce un número válido.")

print("Hola Edson")

try:
    age = int(input("Por favor, introduce tu edad: "))
except:
    age = -1
    print("Tuviste un error al escribir tu edad. Por favor, introduce un número válido.")

if age > 100:
    print("Tienes mas de un siglo de vida")
elif age >= 18 and age <= 100:
    print("Eres mayor de edad.")
elif age < 18 and age >= 0:
    print("Eres menor de edad.")
else:
    print





"""
    Hacer un programa que pregunte la edad de una persona 
    y responda lo siguiente:
        - Si la edd es menor o igual a 4, entonces la entrada
        es gratuita
        -Si la edad es menor o igual a 18, pero mayor a 4
        entonces la entrada cuesta $200
        -Si la edad es mayor que 18, entonces la entrada
        cuesta $400
"""

#Multiple ifs
guisos = ["deshebrada", "asado ", "salsa verde", "pozole"]
if "asado" in guisos:
    print("Hay asado")
else:
    print("No hay asado")
if "Hay tamales" in guisos:
    print("Hay tamales")
else:
    print("No hay tamales")
if "salsa verde" in guisos:
    print("Hay salsa verde")
else:
    print("No hay salsa verde")
if "pozole" in guisos:
    print("Hay pozole")
else:
    print("No hay pozole")
if "deshebrada" in guisos:
    print("Hyay deshebrada")
else:
    print("No hay deshebrada")

