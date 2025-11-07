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
El metodo append() es útil cuando deseas agregar un elemento sin importar su posición en la lista.

"""


print("\n Agregar elementos a una lista usando el metodo append() \n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki']
motorcycles.append("ducati")
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki', 'ducati']

"""

    Agregar elementos a una lista usando el metodo insert()A
    insert() : Agrega un elemento en una posición específica de la lista.
    El metodo insert (index,element) toma dos argumentos:
    el indice donde se desea insertar el elemento y el elemento en si.
    
"""


print("\n Agregar elementos a una lista usando el metodo insert() \n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, "ducati")
print(motorcycles)  # Salida: ['ducati', 'honda', 'yamaha', 'suzuki']
print(motorcycles[0])  # Salida: 'ducati'

# Eliminar elementos de una lista usando del, pop() y remove()
print("\n Eliminar elementos de una lista usando del, pop() y remove() \n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)  # Salida: ['yamaha', 'suzuki']

# Eliminar el ultimo elemento de la lista usando pop()
print("\n Eliminar el ultimo elemento de la lista usando pop() \n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki']
pop_motorcycle = motorcycles.pop()
print(motorcycles)  # Salida: ['honda', 'yamaha']
print(f'La ultima motocicleta eliminada es: {pop_motorcycle}')  # Salida: La ultima motocicleta eliminada es: suzuki

# Eliminar un elemento de una lista con metodo pop(index)
print("\n Eliminar un elemento de una lista con metodo pop(index) \n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
first_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(f'La primera motocicleta eliminada es: {first_motorcycle}')

# Eliminar un elemento de una lista usando remove()
print("\n Eliminar un elemento de una lista usando remove() \n")
motorcycles = ["honda", "yamaha", "suzuki", "ducati", "yamaha"]
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove("yamaha")
print(motorcycles)  # Salida: ['honda', 'suzuki', 'ducati', 'yamaha']

"""

    Metodo built-in
    -print()
    -str()
    -type()

    Metodo de listas
    -.append()
    -.insert()

    Metodo statement
    -del
    -pop()
    -.remove()

"""

# Ejemplo del metodo remove()
names = ['ana ', 'juan', 'pedro', 'luis', 'maria']
print(names)  # Salida: ['ana ', 'juan', 'pedro', 'luis', 'maria']
deleted_name = input ("\n \n Ingrese un nombre para eliminar de la lista: ")
names.remove(deleted_name.strip().lower()) # Elimina el nombre ingresado por el usuario
print(names)  # Salida: ['ana ', 'juan', 'pedro', 'luis', 'maria'] sin el nombre eliminado

# Nota: Si el nombre no existe en la lista, se generará un ValueError.

"""
    Como ordenar listas en Python
    -sort() : Ordena la lista de forma permanente en orden ascendente o descendente

        Ordenamiento permanente, es decir, ordena la lista original y no crea una nueva lista ordenada.
        Por defecto, sort() ordena en orden ascendente (de menor a mayor).

        sort(reverse=True) : Ordena la lista en orden descendente (de mayor a menor).
        sort(reverse=False) : Ordena la lista en orden ascendente (de menor a mayor
"""
print("\n Como ordenar listas en Python \n")
cars = ['bmw', 'audi', 'toyota', 'kia', 'ford', ]
print(cars)  # Salida: ['bmw', 'audi', 'toyota', 'kia', 'ford']
cars.sort(reverse=False)  # Ordena la lista en orden ascendente
print(cars)  # Salida: ['audi', 'bmw', 'ford', 'kia', 'toyota']

motorcycles = ["mortalica","honda","ducatti"]
print(motorcycles)
motorcycles.reverse()
print(motorcycles) # Salida: ['ducatti', 'honda', 'mortalica']

"""
    Cantidad de elementos en una lista
    Metodo built-in len() : Devuelve la cantidad de elementos en una lista
"""
cars = ['ford', 'kia', 'chevrolet']
print("\n Metodo built-in len() \n")
print(len(cars))  # Salida: 3


"""
    Metodo built-in
    Ordena las listas temporalmente sin modificar la lista original
    -sorted() : Ordena la lista temporalmente en orden ascendente o descendente
        sorted(lista) : Ordena la lista en orden ascendente (de menor a mayor)
        sorted(lista, reverse=True) : Ordena la lista en orden descendente (de mayor a menor)
        sorted(lista, reverse=False) : Ordena la lista en orden ascendente (de menor a mayor)
"""
favorite_students = ["jorge", "jose","carlos","emiliano"]
print(favorite_students)  # Salida: ['jorge', 'jose', 'carlos', 'emiliano']

fav_stu_ordened = sorted(favorite_students, reverse=False)  # Ordena la lista en orden ascendente
print("lista ordenada: ",fav_stu_ordened)  # Salida: lista ordenada:  ['carlos', 'emiliano', 'jorge', 'jose']
print("lista original: ",favorite_students)  # Salida: lista original:  ['jorge', 'jose', 'carlos', 'emiliano']

