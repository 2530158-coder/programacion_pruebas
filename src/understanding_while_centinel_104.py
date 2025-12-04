# Centinel: El usuario decide cuando salir del 
# programa y no el mismo programa

"""
    Vamos a realizar un prograam que sume numeros 
    hasta que el usuario escriba la palabra 'salir'

    El programa tambien debde decirme cuantos numeros 
    ingreso el usuario, cuando fue el minimo y cual fue
    el maximo.

"""

sum_of_numbers = 0.0
counter = 0
minimum = None
maximum = None

while True:
    print("Ingresa la palabra 'salir' para salir del loop")
    user_input = input("Ingresa una cantidad en pesos mexicanos")

    # Centinel
    if user_input == "salir":
        break

    try:
        quantity = float(user_input)
    except ValueError:
        print("Cantidad invalida, ingresa nuevamente")
        continue
    except KeyboardInterrupt:
        break
        
    counter += 1  # counter = counter + 1 # Estructura counter
    sum_of_numbers += quantity   # sum_numbers = sum_numbers + quantity # Estrucutura acumuladora

    if minimum is None or quantity < minimum:
        minimum = quantity

    if maximum is None or quantity > maximum:
        maximum = quantity

print("SUM", sum_of_numbers)
print("CONTADOR", counter)
print("Maximo", maximum)
print("MINIMO", minimum)