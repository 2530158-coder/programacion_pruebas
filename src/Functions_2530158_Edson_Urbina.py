"""
    Edson Saeed Urbina Guerrero

    Grupo I-M 1-2 

    Matricula 2530158

"""

# Problema 1:
"""
Descripción:
Define dos funciones:
- calculate_area(width, height): regresa el área de un rectángulo.
- calculate_perimeter(width, height): regresa el perímetro.
El código principal debe leer (o definir) los valores, llamar a las funciones y mostrar los resultados.
"""

def area(width, height):
    return width * height
def perimeter(width, height):
    return 2 * (width + height)
try:
    width = float(input('Set the width of the rectangle: '))
    height = float(input('Set the height of the rectangle: '))
    if width < 0 or height < 0:
        print('Set positive numbers')
    else:
        print(f'The area of the rectangle is: {area(width, height)}')
        print(f'The perimeter of the rectangle is: {perimeter(width, height)}')
except:
    print('Set a real number')

"""
Entradas:
- width: ancho del rectángulo (float)
- height: alto del rectángulo (float)

Salidas:
- Área del rectángulo (float)
- Perímetro del rectángulo (float)

Validaciones:
- width > 0
- height > 0
- Si alguna condición no se cumple, mostrar "Error: invalid input" y no llamar a las funciones.

Casos:
    Set the width of the rectangle: 6
    Set the height of the rectangle: 4
    The area of the rectangle is: 24.0
    The perimeter of the rectangle is: 20.0

    Set the width of the rectangle: -5
    Set the height of the rectangle: 3
    Set positive numbers

    Set the width of the rectangle: abc
    Set the height of the rectangle: 3
    Set a real number
"""
# Problema 2:
"""
Descripción:
Define una función classify_grade(score) que reciba una calificación numérica (0–100) y regrese una categoría:
- "A" si score >= 90
- "B" si 80 <= score < 90
- "C" si 70 <= score < 80
- "D" si 60 <= score < 70
- "F" si score < 60
El código principal debe llamar la función y mostrar el resultado.
"""
def classify_grade(score):
    if score >= 90:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

try:
    score = float(input("Enter the score (0-100): "))
    if 0 <= score <= 100:
        grade = classify_grade(score)
        print(f"The grade is: {grade}")
    else:
        print("Score out of range")
except:
    print('Set a valid number')

"""
Entradas:
- score: calificación numérica (float entre 0 y 100)

Salidas:
- Categoría de la calificación (str: "A", "B", "C", "D", "F")

Validaciones:
- 0 <= score <= 100
- Si no se cumple, mostrar "Error: invalid input" y no clasificar.

Casos:
    Enter the score (0-100): 85
    The grade is: B

    Enter the score (0-100): 105
    Score out of range

    Enter the score (0-100): abc
    Set a valid number
"""
# Problema 3:
"""
Descripción:
Define una función summarize_numbers(numbers_list) que reciba una lista de números y regrese un diccionario con:
- "min": mínimo
- "max": máximo
- "average": promedio (float)
El código principal debe construir la lista (por ejemplo, a partir de texto separado por comas), 
llamar la función y mostrar los valores.
"""
numbers_list = {}
def summarize_numbers(numbers_list):
    minimum = min(numbers_list)
    maximum = max(numbers_list)
    average = sum(numbers_list) / len(numbers_list)
    return {
        "min": minimum,
        "max": maximum,
        "average": average
    }

try:
    quantity = int(input("How many numbers will you enter? "))
    if quantity <= 0:
        print("Enter a positive number")
    else:
        numbers = []
        for _ in range(quantity):
            num = float(input("Enter a number: "))
            numbers.append(num)
        suma = summarize_numbers(numbers)
        print(f"suma: Min = {suma['min']}, Max = {suma['max']}, Average = {suma['average']}")
except:
    print("Set a valid number")

"""
Enrtadas:
- numbers_list: lista de números (list of float)

Salidas:
- Diccionario con "min", "max", "average" (dict)

Validaciones:
- numbers_text no vacío tras strip().
- Lista no vacía después de la conversión.
- Todos los elementos deben poder convertirse a números; si alguno falla, mostrar "Error: invalid input".

Casos:
    How many numbers will you enter? 4
    Enter a number: 10
    Enter a number: 20
    Enter a number: 30
    Enter a number: 40
    suma: Min = 10.0, Max = 40.0, Average = 25.0

    How many numbers will you enter? 0
    Enter a positive number

    How many numbers will you enter? abc
    Set a valid number
"""
# Problema 4:
"""
Descripción:
Define una función apply_discount(prices_list, discount_rate) que:
- reciba una lista de precios (float) y una tasa de descuento (por ejemplo, 0.10 para 10%)
- regrese una nueva lista con los precios ya descontados (no modificar la lista original).
El código principal debe:
- Crear una lista de precios.
- Llamar a la función.
- Mostrar la lista original y la nueva lista con descuento.
"""
def apply_discount(prices_list, discount_rate):
    discounted_prices = []
    for price in prices_list:
        discounted_price = price * (1 - discount_rate)
        discounted_prices.append(discounted_price)
    return discounted_prices

try:
    quantity = int(input("How many prices will you enter? "))
    if quantity <= 0:
        print("Enter a positive number")
    else:
        prices = []
        for _ in range(quantity):
            price = float(input("Enter a price: "))
            prices.append(price)
        discount_rate = float(input("Enter the discount rate (e.g., 0.10 for 10%): "))
        if discount_rate < 0 or discount_rate > 1:
            print("Enter a valid discount rate between 0 and 1")
        else:
            discounted_prices = apply_discount(prices, discount_rate)
            print(f"Original prices: {prices}")
            print(f"Discounted prices: {discounted_prices}")
except:
    print("Set a valid number")

"""
Entradas:
- prices_list: lista de precios (list of float)
- discount_rate: tasa de descuento (float entre 0 y 1)

Salidas:
- Nueva lista con precios descontados (list of float)

Validaciones:
- prices_text no vacío y lista resultante no vacía.
- Todos los precios > 0.
- 0 <= discount_rate <= 1; si no, "Error: invalid input".
"""