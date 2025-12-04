"""
    Si el año es divisible entre 4, es bisiesto 
    Pero si es divisible entre 100 no es bisiesto
    Pero si es divisible entre 400 si es bisiesto

"""
try:
    

    year = int(input("Insert your year"))


    if year % 4 == 0 and year % 100 == 0:
        print("El año no es bisiesto")
    elif year % 4 == 0:
        print("El año es bisiesto")
    elif year % 4 == 0 and year % 400 == 0:
        print("El año es bisiesto")

    else:
        print("El año no es bisiesto")
    
except ValueError: 
    print("Por favor, introduce un número válido.")


try:
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            print("si")
        elif year % 100 == 0:
            print("no")
        else:
            print("si")
    else:
        print("no")
except ValueError:
    print("camote")

