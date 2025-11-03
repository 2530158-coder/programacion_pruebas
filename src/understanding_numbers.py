#Numbers 

"""

Integers = - Enteros

'
Son numeros sin punto decimal
-Infty , ...,-3,-2,-1,0,1,2,3,... , +Infty


# Tipado dinamico
Ejemplo : 

age = 33

numero flotante
Son numeros con punto decimal
- Infty , ...,-3.5,-2.0,-1.1,0.0,0.1,1.5,2.3,3.8,... , +Infty

number_2 = 0.3


Los podemos sumar(++), restar(--), multiplicar(**), dividir(//) y mucho mas.    

potenciacion(**), modulo(%), division entera(//)

potencia : Es elevar un numero a otro numero

potencia (base, exponente)
potencia(2,3) = 8

Modulo: Es el resto de una division

Modulo (dividendo, divisor)
Modulo(10,3) = 1

Modulo (14,5) = 4

Modulo es usado para determinar si un numero es par o impar

"""
print(0.1 + 0.2)  # Ejemplo de suma de floats

number_1 = 33
number_2 = 13

suma = number_1 + number_2

resta = number_1 - number_2

multiplicacion = number_1 * number_2

division = number_1 / number_2

potencia = number_1 ** 2

modulo = number_1 % 2  # Determina si es par o impar

print("Suma: ", suma)
print("Resta: ", resta)
print("Multiplicacion: ", multiplicacion)
print("Division: ", division)
print("Potencia: ", potencia)
print("Modulo (Determina si es par o impar): ", modulo)

print("la suma es de tipo " ,type(suma))
print("la resta es de tipo " ,type(resta))
print("la multiplicacion es de tipo ", type(multiplicacion))
print("la division es de tipo ", type(division))
print("la potencia es de tipo ", type(potencia))
print("el modulo es de tipo ", type(modulo))


## Imprimir edad de alguien

age = 33
message= "Charly tiene + age + años" 
print("edad", age)

"""
TypeError: Python no puede reconocer el tipo 
de informacion que se esta utilizando dentro de las comillas
para concatenar diferentes tipos de datos.

Para convertir a string utilizo: str()

"""
message_f = f"Charly tiene {age} años"
print(message_f)


