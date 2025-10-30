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
