"""
Edson Saeed Urbina Guerrero
Grupo I-M 1-2 104
Matricula 2530158
"""

# Problema 1:
print('\n\n\n Problema 1\n')
"""
Calcula la suma de todos los enteros desde 1 hasta n (incluyendo n). 
Además, calcula la suma solo de los números pares en ese mismo rango usando un bucle for.

Entradas:
- n (int; límite superior del rango).

Salidas:
- "Sum 1..n:" <total_sum>
- "Even sum 1..n:" <even_sum>

Validaciones:
- Verificar que n pueda convertirse a int.
- n >= 1; si no se cumple, mostrar "Error: invalid input".
"""
suma = 0
even = 0
try:
  n = int(input('Set your final numbers to sum'))
  for number in range(0, n+1):
    suma = suma + number
  for number in range(0, n+1, 2):
    even = even + number
except:
  print('Set real number')
print(f'The sum is {suma}')
print(f'The sum of even is {even}')

# Problema 2:
print('\n\n\nProblema 2: \n')
"""

Genera y muestra la tabla de multiplicar de un número base, 
desde 1 hasta un límite m. 
ejemplo, si base = 5 y m = 4, muestra:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20

Entradas:
- base (int)
- m (int; límite de la tabla)

Salidas:
- Línea por cada multiplicación:
  - "5 x 1 = 5"
  - "5 x 2 = 10"
  - etc.

Validaciones:
- base y m convertibles a int.
- m >= 1; si no, "Error: invalid input".

"""
base = int(input('Set the base of the multiplication: '))
limit = int(input("Set the limit of the multiplications: "))
for number in range(1, limit+1):
  multiplication = base * number
  print(f'{base} x {number} = {multiplication}')

# Problema 3:
print('\n\n\n Problema 3: \n')
"""
Lee números uno por uno hasta que el usuario ingrese un valor sentinela (por ejemplo, -1). 
Calcula el promedio de los números válidos ingresados y la cantidad de números leídos. 
Si el usuario sólo ingresa el sentinela sin números válidos, muestra un mensaje de error.

Entradas:
- number (float; se lee repetidamente).
- sentinel_value (fijo en el código, por ejemplo: -1).

Salidas:
- "Count:" <count>
- "Average:" <average_value>
- Si no se ingresan datos válidos:
  - "Error: no data"

Validaciones:
- Cada lectura debe intentar convertirse a float.
- Ignorar el sentinela en los cálculos.

"""
try: 
    centinela = 0
    suma = 0
    count = 0
    while centinela != -1:
        centinela = int(input('Set a number'))
        if centinela != -1:
            suma = suma + centinela
            count = count + 1
    if count == 0:
        print("Error, you don't set any number before the centinel")
    else:
        print(f'The sum of the numbers is {suma}')
        average = suma / count
        print(f'The average is {average}')
except:
    print('error in problem 3')

# Problema 4:
print('\n\n\n Problema 4: \n')
"""
Implementa un sistema sencillo de intento de contraseña. 
Define en el código una contraseña correcta (por ejemplo, "admin123"). 
El usuario tiene un máximo de MAX_ATTEMPTS intentos para introducirla. 
Si acierta dentro del límite, mostrar un mensaje de éxito. 
Si agota los intentos, mostrar un mensaje de bloqueo.

Entradas:
- user_password (string; se lee en cada intento).

Salidas:
- Si acierta:
  - "Login success"
- Si falla todos los intentos:
  - "Account locked"

Validaciones:
- MAX_ATTEMPTS > 0 (definido como constante en el código, por ejemplo 3).
- Contar correctamente los intentos.

"""
attemps = 3
PIN = 1234
while attemps != 0:
    try:
        password = int(input('Set your password: '))
        if len(str(password)) == 4:
            if password == PIN:
                print('acceso permitido')
                break
            else:
                print('intenta otra vez')
                attemps = attemps -1
        else:
            print('Set 4 digits')
            attemps = attemps - 1
    except:
        print('Set a real PIN')
        attemps = attemps - 1   
    print(f'you have {attemps} attemps more')
    if attemps == 0:
        print('acces denied')

# Problema 5:
print('\n\n\n Problema 5: \n')
"""
Implementa un menú de texto que se repite hasta que 
el usuario seleccione la opción de salir.
 Ejemplo de menú:
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit 
El programa debe ejecutar la acción correspondiente a cada opción y 
volver a mostrar el menú hasta que se elija 0.

Entradas:
- option (string o int; elección del usuario).

Salidas:
- Mensajes según la opción:
  - "Hello!" para saludo.
  - "Counter:" <counter_value> para mostrar contador.
  - "Counter incremented" al incrementar.
  - "Bye!" al salir.
- Para opciones inválidas:
  - "Error: invalid option"

Validaciones:
- Normalizar option (por ejemplo, convertir a int con manejo de error).
- Asegurar que sólo 0,1,2,3 sean aceptadas como válidas.

"""
import time
import random
option = 's'

while option != '0':
  time.sleep(0)
  print('\n Set 1 to show a poem')
  print('Set 2 to show a random number')
  print('Set 3 to print the numbers in range(1, 10000000000)')
  print('Set 0 to exit')
  option = input('-  ')
  if option == '1':
    time.sleep(1)
    print('hola')
    time.sleep(1)
    print('camote')
    time.sleep(1)
    print('FIN')
    time.sleep(5)
  elif option == '2':
    rand = random.randint(0, 10000)
    print(rand)
  elif option == '3':
    time.sleep(4)
    print('1')
    time.sleep(3)
    print('the numbers in range(1, 10000000000)')
    print('FIN')
    time.sleep(1)

# Problema 6
print('\n\n\n Problema 6: \n')
"""
Usa bucles for anidados para imprimir un patrón de asteriscos
 en forma de triángulo rectángulo. Por ejemplo, para n = 4:
*
**
***
****
Además, imprime un segundo patrón invertido 
(opcional si lo deseas extender, pero documenta tu decisión).

Entradas:
- n (int; número de filas del patrón).

Salidas:
- Patrón línea por línea:
  - "*"
  - "**"
  - "***"
  - "****"
- (Opcional) Patrón invertido si se implementa.

Validaciones:
- n convertible a int.
- n >= 1; si no, "Error: invalid input".
"""

quantity = int(input('Set the quantity of lines: '))
list_of_numbers = list(value for value in range(1, quantity+1))
for number in list_of_numbers:
  print('*' * number)
list_of_numbers.sort(reverse=True)
for number in list_of_numbers:
  print('*' * number)
