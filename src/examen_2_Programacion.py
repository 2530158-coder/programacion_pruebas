# Area y perimetro de rectangulo
print("\n Programa de area y perimetro de rectangulo")

b_1 = float(input("\n Pon tu base: "))
h_1 = float(input("\n Pon tu altura: "))

if b_1 < 0 or h_1 < 0:
    print("\n Error: invalid input")
else:
    area_1 = b_1*h_1
    perimeter_1 = 2*b_1 + 2*h_1

    print(f"\n Tu area es: {area_1}")
    print(f"\n Tu perimetro es: {perimeter_1}")

# Fibonacci
while True:

    numbers = [0,1]
    try:
        posicion = int(input("\n Ingresa tu posicion: "))

        for coordenada in range(1, posicion-1):
            n = numbers[-1] + numbers[-2]
            numbers.append(n)
        for numero in numbers:
            print(numero)
    except ValueError:
        print("\n Ocurrio un error")
        break
    except KeyboardInterrupt:
        print("\n Se utilizo Ctr+C")
        break