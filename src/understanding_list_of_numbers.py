"""
    Las listas pueden almacenar numeros y de hecho
    son ideales para almacenarlos.
    Python ofrece cantidad de funciones integradas
    para trabajar con listas de numeros.

    Por ejemplo, podemos usar la funcion range()
    para generar una lista de numeros en un rango
    determinado.


"""

# Laa funcion range() genera una secuencia de numeros
# desde un valor inicial hasta un valor final (exclusivo).

#Por ejemplo, para generar una lista de numeros del 0 al 9:
numbers = list(range(10))
print("Numeros del 0 al 9:", numbers) #Salida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(numbers)) #Salida: <class 'list'>


# Podemos realizar lo mismo con un for loop:

print("\n Numeros del 0 al 9 usando for loop:")
for num in range(10):
    print(num, end=' ')  #Salida: 0 1 2 3 4 5 6 7 8 9
    print(type(num))  #Salida: <class 'int'>



print("\n Numeros 1 al 5")
for num in range(1, 5):
    print(num, end=' ')  #Salida: 1 2 3 4
numbers_1_to_4 = list(range(1, 5))
print("\n Lista de numeros del 1 al 4:", numbers_1_to_4) #Salida: [1, 2, 3, 4]


print("\n Numeros impares, 1 al 9 con paso de 2")
for num in range(1, 10, 2): # Numeros impares del 1 al 9
    print(num, end=' ')  #Salida: 1 3 5 7 9
odd_numbers = list(range(1, 10, 2))
print("\n Lista de numeros impares del 1 al 9:", odd_numbers) #Salida: [1, 3, 5, 7, 9]


print("\n Numeros pares, 2 al 8 con paso de 2")
for num in range(2, 10, 2): # Numeros pares del 2 al 8
    print(num, end=' ')  #Salida: 2 4 6 8
even_numbers = list(range(2, 10, 2))
print("\n Lista de numeros pares del 2 al 8:", even_numbers) #Salida: [2, 4, 6, 8]

# Podemos usar funciones integradas como sum(), min(), max()
# para trabajar con listas de numeros.

#Podemos crear todo tipo de listas de numeros usando range() y list().
print("\n Primeros 10 numeros al cuadrado:")
squares = []
for value in range(1, 11):
    square = value ** 2 # Elevar al cuadrado
    squares.append(square)
print(squares)  # Salida: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Podemos simplificar el codigo anterior usando una sola linea
print("\n Primeros 10 numeros al cuadrado (usando list comprehension):")
squares = [value ** 2 for value in range(1, 11)]
print(squares)  # Salida: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


"""
    Metodos built-in para listas de numeros
    min(): Devuelve el valor minimo en una lista de numeros
    max(): Devuelve el valor maximo en una lista de numeros
    sum(): Devuelve la suma de todos los numeros en una lista

"""
# Metodo built-in para listas de numeros 
print("\n Metodos built-in para listas de numeros:")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"Lista de digitos: {digits}")  # Salida: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Minimo:", min(digits))  # Salida: 0
print("Maximo:", max(digits))  # Salida: 9
print("Suma:", sum(digits))  # Salida: 45