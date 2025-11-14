print("\n\t listas con el metodo for")
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# El condicional es el corazon de un if
# Condicional true

car = "bmw"
print (car == 'bmw')  # True   

# Condicional false
car = "Audi"
print (car == 'audi')  # False

# Posible solucion a las entradas del usuario
car = "Audi"
print(car.lower() == 'audi')  # True

# Operador relacional != para determinar si dos valores no son iguales
requested_topping = 'mushrooms'
if requested_topping != 'anchovies': #True, significa que no hay anchoas
    print("Hold the anchovies!")


# Comparaciones numericas
age = 18 # entero
print(age == 18)  # True

answer = 17
if answer != 42:
    print("Esa no es la respuesta correcta, intenta de nuevo porfavor!")

age = 17
print(age < 21)  # True
print(age <= 21)  # True
print(age > 21) # False
print(age >= 21) #False

# multiples condiciones
age_0 = 22
age_1 = 18
#Operation_and
print(age_0 >= 21 and age_1 >= 21) # False
print(age_0 >= 21 and age_1 <= 21)  # True
#Operation_or
print(age_0 >= 21 or age_1 >= 21)  # True
print(age_0 >= 23 or age_1 >= 21)  # False

"""
    Para preguntarnos si un valor se encuentra en una lista 
    usamos la palabra reservada in

    valor_in_lista = valor in lista
    Si el valor se encuentra en la lista, la expresion devolvera True
    si no, devolvera False

"""
motorcycles = ['mortalica', 'honda', 'vento', 'yamaha']
motor_charly_wants = "italica"
print(motor_charly_wants in motorcycles)  # False
print("honda" in motorcycles) #True



"""
    Para preguntarnos si un valor no se encuentra en una lista
    usamos la palabra reservada not in

    value_no_en_lista = valor not in lista
    Si el valor no se encuentra en la lista, la expresion devolvera True

"""
banned_students = ['Jorge', 'Carlos', 'moyra', 'gus', 'hots']
user = "mauro"
print(user not in banned_students)  # True
print("gerardo" not in banned_students)  # True

print("jorge" not in banned_students) # False

# Variables booleanas
game_active = True
can_edit = False

"""
    if statement
    Una estructura condicional que permite ejecutar un bloque de codigo

    single_if_statement:

    if condicion:
        do something

    if something:
        do something

    else:
        do something else

"""



#if statement

age = (input("Enter your age: "))
print(type(age))


if int(age)  >=18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote.")