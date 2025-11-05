# LISTAS EN PYTHON
# Las listas son estructuras de datos que permiten almacenar múltiples valores en una sola variable.
# Son mutables, lo que significa que se pueden modificar después de su creación.
# Se definen utilizando corchetes [] y los elementos se separan por comas.
# Ejemplo de creación y manipulación de listas en Python:
fruits = ["manzana", "banana", "cereza", "naranja"]
print(fruits)  # Salida: ['manzana', 'banana', 'cereza', 'naranja']

# Agregar un elemento a la lista
fruits.append("naranja")
print(fruits[0].upper())  # Acceder al primer elemento: 'manzana'   
print(fruits[1].title())  # Acceder al segundo elemento: 'banana'
print(fruits[2])  # Acceder al tercer elemento: 'cereza'
print(fruits[3]) # Acceder al cuarto elemento: 'naranja'

# print(fruits[3]) generaria un error IndexError si la lista no tuviera un cuarto elemento


#Acceder al cuarto elemento: 'naranja'
print(fruits[-1])  # Acceder al último elemento: 'naranja'
print(fruits[-2])  # Acceder al penúltimo elemento: 'cereza'
print(fruits[-3]) # Acceder al antepenúltimo elemento: 'banana'
print(fruits[-4])  # Acceder al cuarto elemento desde el final: 'manzana' 

my_favorite_fruit = fruits[0]
message = f"My favorite fruit is {my_favorite_fruit[0].title()}."
print(message) # Salida: Mi fruta favorita es Manzana

# Modificar un elemento de la lista
fruits[1] = "kiwi"
print(fruits)  # Salida: ['manzana', 'kiwi', 'cereza', 'naranja', 'naranja']

#Agregar un elemento en una posición específica
fruits.insert(2, "mango")
print(fruits)  # Salida: ['manzana', 'kiwi', 'mango', 'cereza', 'naranja', 'naranja']


"""

Agregar elementos a una lista usando el metodo append()
- Append() : Agrega un elemento al final de la lista.


"""


print("\n Agregar elementos a una lista usando el metodo append() \n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki']
motorcycles.append("ducati")
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki', 'ducati']

"""

    Agregar elementos a una lista usando el metodo insert()A
    insert() : Agrega un elemento en una posición específica de la lista.

"""


print("\n Agregar elementos a una lista usando el metodo insert() \n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, "ducati")
print(motorcycles)  # Salida: ['ducati', 'honda', 'yamaha', 'suzuki']
print(motorcycles[0])  # Salida: 'ducati'