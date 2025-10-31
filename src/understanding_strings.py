"""

Un string es de manera sencilla una serie de caracteres.
En python todo lo que se encuentre entre comillas simples 
'' o dobles comillas " es considerado un string.

""Esto es un string"
'Esto tambien es un string'

'Le dije a un amigo, "¡Python es mi lenguaje favorito!"'
"El lenguaje 'Python' lleva el nombre por Monty Pythob,
no por la serpiente"" 

"""

name = "clase de programacion"
print(name)
print(name.title())
print(name)


"""

Un metodo es una accion que python puede realizar 
en un fragmento de datos o sobre una variable.

El punto. despues de una variable seguida
del metodo tittle() dice que se tiene que ejecutar
el metodo tittle() de la variable name.

Todos los metodos van seguidos de parentesis
porque en ocasiones necesitan informacion adicional
para funcionar, en esta ocasion el metodo tittle() no requiere 
informacion adicional para ejecutarse.


"""

print(name.upper())
print(name.lower())

# Concatenacion de STRINGS
print("CONCATENACION DE STRINGS")

first_name = "charly"
last_name = "mercury"
full_name = first_name +" "+ last_name
print(full_name)

print("Hola, " + full_name.title() + "!")

#Sintax error con strings
message = "Una fortaleza de python es su comunidad"
print(message)

message_two = "Una fortaleza de 'Python' es su comunidad"
print(message_two)

#Concatenacion con f-String
famous_person = "Charly Mercury"
quote = "Python is love"

message = famous_person +" una vez dijo "+ quote
print(message)

#Concatenacion con string
message_f_string = f"{famous_person} una vez dijo {quote}"
print(message_f_string)

#Actividad
"""
1) Elige una persona famosa = una variable
2) Elige una frase famosa que haya dicho
3)Genera un mensaje con las 2 variables con f_strings
4)Imprime el mensaje

"""

persona_famosa = "CR7"

frase = "'Si Dios no le agrada a todo el mundo, ¿como lo voy a conseguir yo?'"

message_f_strings = f"{persona_famosa} una vez dijo {frase}"
print(message_f_strings)

persona = "Jhonatan"

frase_2 = "'pero si estan bonitas, ¿o no?'"


message_f_strings_2 = f"{persona} una vez dijo {frase_2}"
print(message_f_strings_2)