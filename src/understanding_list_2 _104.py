#Slicing
print("\n\t Lista de jugadores conn el metodo SLICING")
players = ["CR7", "MESSI", "Travis", 'chicha_god', "corona"]
print(f"\n {players[0:3]}")
#Slice es trbajar con un grupo en especifico
# de elementos de una lista
print(f"\n {players[1:4]}") # ['MESSI', 'Travis', "chicha-god"]
print(f"\n {players[:4]}") # playes = ["CR7", "Travis", "chicha-god"]
print(f"\n {players[:2]}") # players = ["CR7", "MESSI"]

print(f"\n {players[-3:-1]}") # players = ["Travis", 'chicha-god']

#Slicing en for
players = ["CR7", "MESSI", "Travis", 'chicha_god', "corona"]
first_three_player = players[0:4]
print("\n\tFirst three players", first_three_player)

print("\n\tAqui vienen los tres mejores del salon: ")
for player in players[0:3]:
    print(f"\n\t{player}")

# Students
students = ["Axel", "Ignacio", "Jhonatan", "Jorge"]
Best_students = students[0:3]
print("\n\tFirst three students", students)

print("\n\tBest students of the classrrom: ")
for student in students[0:3]:
    print(f"\n\t{student}")

# Copia de listas
print("\n Como copiar listas?")
print(f"\n\n\t lista original")
my_food = ['pizza', 'gorditas de jaumave', 'machacado']
print(f"\n\n {my_food}")
#copy_of_food = my_food # Manera erronea de copiar en una lista
print("\n\n\t Copia de la lista con  corchete")
copy_of_food = my_food[:]
print(f"\n\n {copy_of_food}")

print("\n\n\t Copia de la lista con metodo 'copy.()'")
copy_of_food = my_food.copy()
print(f"\n\n {copy_of_food}")

print("\n\n\t Copia de lista con metodo list()")
copy_of_food = list(my_food)
print(f"\n\n {copy_of_food}")


"""
    Listas : Conjunto de datos mutables

    Duplas : Almacenamiento de datos inmutables 

"""


# Modificando elementos
print("\n\n\t Lista de coches")
cars = ["bwm", "porch", "masda", "totoya", "ford"]
print(f"\n\n {cars}")
cars [0]= "bmw"
cars [1] = "porsh"
cars [2] = "mazda"
cars [3] = "toyota"
print(f"\n\n {cars} ")
