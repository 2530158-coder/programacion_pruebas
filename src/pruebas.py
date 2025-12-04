ed_1 = "Prueba de Edson"
print(ed_1.split())

yop = "Edson Urbina Guerrero"
print(yop.islower()) # False
print(yop.isupper())  # False
yop = yop.lower()
print(yop.isalnum()) # False
print(yop.isalpha())  # False


# 6.1 Problem: Fibonacci series up to n terms

numbers = [0,1]
posicion = int(input("Pon tu coordenada"))
for coor in range(1, posicion-1):
    n = numbers[-1] + numbers[-2]
    numbers.append(n)
for number in numbers:
    print(number) 





