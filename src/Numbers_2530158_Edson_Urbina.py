# 1 Temperature converter and range flag
"""
  Edson Saeed Urbina Guerrero
  Grupo I-M 1-2 104
  Matricula 25 30158
"""

"""
        Convierte una temperatura en grados Celsius (float) a Fahrenheit y Kelvin. Además, determina un valor booleano is_high_temperature que sea true si la temperatura en Celsius es mayor o igual que 30.0 y false en caso contrario.

        Entradas:
        - temp_c (float; temperatura en °C).

        Salidas:
        - "Fahrenheit:" <temp_f>
        - "Kelvin:" <temp_k>
        - "High temperature:" true|false


"""
while True:
        print("\n Welcome to the temperature converter program")
        try:
                temp_c = float(input("\n temperature C"))

                temp_f = temp_c*9/5 + 32
                temp_k = temp_c+273.15
                
                print(f"Grados Farenheight{temp_f}")
        
                if temp_k < 0:
                        print("Prueba otra vez")
                else:
                        print(f"Grados Kelvin{temp_k}")

                if temp_c > 30:
                        print("Temperatura alta")
                else:
                        print("Temperatura baja")
                        
        except ValueError:                        
                print("Intenta de nuevo")
                break
        except KeyboardInterrupt:
                break

"""
        Validaciones:
        - Verificar que temp_c pueda convertirse a float.
        - No permitir temperaturas físicas imposibles en
        Kelvin (por ejemplo, temp_k < 0.0).


"""
# 2 Work ours calculator

"""
Calcula el pago total semanal de un trabajador. Hasta 40 horas se pagan a hourly_rate (float). Las horas extra (> 40) se pagan al 150% de la tarifa normal. Además, genera un booleano has_overtime que indique si el trabajador hizo horas extra.

Entradas:
- hours_worked (float; horas trabajadas en la semana).
- hourly_rate (float; pago por hora).

Salidas:
- "Regular pay:" <regular_pay>
- "Overtime pay:" <overtime_pay>
- "Total pay:" <total_pay>
- "Has overtime:" true|false
"""

hours_worked = float(input("Ingresa tus horas"))
hourly_rate = float(input("Ingresa tu pago por hora"))

regular_pay = hours_worked * hourly_rate
print(f" Pago normal {regular_pay}")
if hours_worked > 40:
    
    overtime_hours = hours_worked - 40
    print(f" Horas extra trabajadas: {overtime_hours}")

    overtime_pay = overtime_hours * hourly_rate * 1.5
    print(f" Horas extra pagadas: {overtime_pay}")

    Total_pay = regular_pay + overtime_pay
    print(f" Pago total: {Total_pay}")
else:
    print(f" Tu pago normal es {regular_pay} ")

"""
Validaciones:
- hours_worked >= 0
- hourly_rate > 0
- Si alguno no cumple, mostrar "Error: invalid input".
"""

# 3 Discount eligibility with booleans
"""
  Determina si un cliente obtiene un descuento en su compra. La regla es:
  - Tiene descuento si:
  - is_student es true OR
  - is_senior es true OR
  - purchase_total >= 1000.0
  Calcula también el total a pagar aplicando un 10% de descuento cuando sea elegible.

  Entradas:
  - purchase_total (float; total de la compra).
  - is_student_text (string; "YES" o "NO").
  - is_senior_text (string; "YES" o "NO").

  Salidas:
  - "Discount eligible:" true|false
  - "Final total:" <final_total>
"""

purchase = float(input("Total de compras"))
is_student_text = input("Eres estudiante SI O NO")
is_senior_text = input("Eres señor SI O NO")

if is_student_text.upper().strip()== "SI" or is_senior_text.upper().strip() == "SI" or purchase >= 1000.0:
    purchase_total = purchase - purchase * 0.1
    print(purchase_total)

else:
    print(f"No se aplica descuento a {purchase}")

"""
Validaciones:
- purchase_total >= 0.0
- Normalizar is_student_text e is_senior_text a mayúsculas y convertir a booleanos is_student, is_senior.
- Si el texto no es "YES" ni "NO", mostrar "Error: invalid input".
"""
# Problem 4: Basic statistics of three integers
print('\n\n\n Problema 4: \n')
"""
Lee tres números enteros y calcula: suma, promedio (float), valor máximo, valor mínimo y 
un booleano all_even que indique si los tres números son pares.
"""
try:
  all_even = False
  num1= int(input('Set your first number '))
  num2= int(input('Set your second number '))
  num3= int(input('Set your third number '))
  suma = num1 + num2 + num3
  average = suma / 3
  list_of_numbers = []
  list_of_numbers.append(num1)
  list_of_numbers.append(num2)
  list_of_numbers.append(num3)
  list_of_numbers.sort(reverse=False)
  if num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2== 0:
    all_even = True
  if all_even:
    print('All numbers are even')
  else:
    print('Some number is odd')
  print(f'The sum of your numbers is {suma}')
  print(f'the average is {average}')
  print(f'The big number is {list_of_numbers[-1]}')
  print(f'The small number is {list_of_numbers[0]}')
except:
  print('Error in something')

# Problema 5: Loan eligibility (income and debt ratio).
print('\n\n\n Problema 5: \n')
"""
Determina si una persona es elegible para un préstamo con base en:
- monthly_income (float)
- monthly_debt (float)
- credit_score (int)
La regla es:
- debt_ratio = monthly_debt / monthly_income
- eligible es true si:
  - monthly_income >= 8000.0 AND
  - debt_ratio <= 0.4 AND
  - credit_score >= 650
"""
try:
  monthly_income = float(input('Set your monthly income: '))
  monthly_debt = float(input('Set your monthly debt: '))
  credit_score = int(input('Set your credit score: '))
  debt_ratio = monthly_debt / monthly_income
  candidate= 0
  if monthly_income >= 8000:
    candidate = candidate + 1
  else:
    print("You don't have good income")
  if debt_ratio <= 0.4:
    candidate = candidate + 1
  else:
    print("You don't have good debt radio")
  if credit_score >= 650:
    candidate = candidate + 1
  else:
    print("You haven't good credit score")

  if candidate == 3:
    print('You have all requirements, you gain the loan')
except:
  print('Set a real number')
  
# Problema 6:  Body Mass Index (BMI) and category flag
print('\n\n\n Problema 6: \n')
"""
Calcula el índice de masa corporal (BMI) de una persona con la fórmula:
- bmi = weight_kg / (height_m * height_m)
Además, genera booleanos para indicar:
- is_underweight (bmi < 18.5)
- is_normal (18.5 <= bmi < 25.0)
- is_overweight (bmi >= 25.0)

"""
try:
  weight = float(input('set your weight in kilograms: '))
  height = float(input('Set your height in meters: '))
  bmi = weight / (height * height)

  if bmi < 18.5:
    print(f'You are underweight, your bmi is {bmi}')
  elif bmi >= 18.5 and bmi < 25:
    print(f'You are normal, your bmi is {bmi}')
  elif bmi >= 25:
    print(f'You are overweight, your bmi is {bmi}')
except:
  print('Set real numbers')

"""
  Conclusion: El uso de metodos y built_in de 
  tipo entero y float nos permite crear codigos 
  que requieran de numeros enteros o decimales, tranformando 
  los strings con int o float(ejemplo: int(input("5")),
  y esto se puede aplicar para necesidades comunes como
  saber tu peso. 
"""

"""
  Referens: https://ellibrodepython.com/python-pep8
  https://javascript.info/coding-style
  https://www.codecademy.com/
  
"""