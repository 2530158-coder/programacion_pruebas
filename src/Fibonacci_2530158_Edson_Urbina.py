"""
    Implementa un programa que calcule y muestre la serie de Fibonacci hasta n términos, donde n es ingresado por el usuario. La serie debe comenzar en 0 y 1, por lo que:

- Si n = 1 → salida: 0  
- Si n = 2 → salida: 0, 1  
- Si n = 7 → salida: 0, 1, 1, 2, 3, 5, 8  

El programa debe:
1) Leer n desde la entrada estándar.  
2) Validar n.  
3) Generar la serie de Fibonacci con un bucle (for o while).  
4) Imprimir los términos en una sola línea, separados por espacios o comas.

Entradas:
- n (int; número de términos de la serie a generar).

Salidas:
- "Number of terms:" <n> (opcional)
- "Fibonacci series:" <term_1> <term_2> ... <term_n>

Validaciones:
- n debe poder convertirse a entero.
- n >= 1.
- (Opcional) n <= 50 para evitar series demasiado grandes; si no se cumple
, mostrar "Error: invalid input".
- Si la validación falla, NO calcular la serie.

"""

# Fibonacci series
while True:
    numbers = [0,1]

    try:
        coordenada = int(input("\n Ingresa tu coordenada: "))
        if coordenada <=50:
            for pos in range(1, coordenada-1):
                n = numbers[-1] + numbers[-2]
                numbers.append(n)
            for numero in numbers:
                print(numero)
        else:
            print("Error, dato demasiado grande")
            break
    except ValueError:
        print("\n Error,invalid input")
        continue
    except KeyboardInterrupt:
        print("\n KeyBoard usada, se interrumpio el programa")
        break