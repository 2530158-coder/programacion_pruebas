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


age = int(input("Insert your age"))


if age <= 4 and age > 0:
    print("La entrada es gratis")

elif age <= 18 and age > 4:
    print("La entrada cuesta $200")

elif age > 18:
    print("La entrada cuesta $400")
    
elif age <= 0:
    print("¿Te falla el cerebro?")






