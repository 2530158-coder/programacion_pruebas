age = 18


message =f"\t nacho tiene {age} años"
print(message.title())

print("\n\t y tiene que hacer el servicio militar")

persona = " MOB Psycho"
mensaje_motivacional = '"eres el protagonista de tu propia vida"'
message_two = f"\t{persona} dijo una vez {mensaje_motivacional} "
print(message_two.rstrip())

ent = "Hola"
ero = "Como estas"

ent_ero = ent +" "+ ero
print(ent_ero)

print("¡" + ent_ero.upper() + "!")
print("¡" + ent_ero.lower() + "!")

print("\n\t Calculadora")

# Define los valores

number_1 = int(input ("\n\t Ingrese el primer valor numerico"))
number_2 =  int(input ("\n\t Ingrese el segundo valor numerico"))

# Operaciones

suma = number_1 + number_2

resta = number_1 - number_2 

producto = number_1 * number_2

division = number_1 / number_2

potencia = number_1 **2

modulo = number_1 % 2

print("\n\t Resultados")

print("Resultado de Suma", suma)
print("Resultado de diferencia", resta)
print("Resultado de Producto", producto)
print("Resultado de Division", division)
print("Resultado de Potencia", potencia)
print("Resultado de modulo", modulo)

# listas

personajes = ["Mario, Link, Pikachu, Donkey-Kong"]
print(personajes)


