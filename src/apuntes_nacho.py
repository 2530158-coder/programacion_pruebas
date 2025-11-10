
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

