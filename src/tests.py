numbers = [0,1]

posicion = int(input("Pon tu coordenada"))

for inventado in range(1,posicion-1):
    n = numbers[-1] + numbers[-2]
    numbers.append(n)
for numero in numbers:
    print(numero)