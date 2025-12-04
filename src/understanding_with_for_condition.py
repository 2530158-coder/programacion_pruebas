"""
    Vamos a realizar un programa 
    que defina un PIN como contraseña

    Despues vamos a darle 3 intentos al
    usuario para escribir el pin

    Si el usuario escribe correctamente el
    pin, el programa dece mostrar un
    mensaje de Acceso Permitido

    Si el usuario se equivoca el preogramam
     debe de decir

"""

CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3
intents = 0

while intents < MAX_ATTEMPTS:
    
    user_pin = input("Escribir tu pin")
    if user_pin ==  CORRECT_PIN:
        print("Acceso permitido")
        break
    else:
        intents += 1
        remaining_attemps = MAX_ATTEMPTS-intents
        if remaining_attemps>0:
            print(f"PIN incorrecto, te quedan{remaining_attemps} intentos")
        else:
            print("Acceso denegado")

print("Final")
