"""
Edson Saeed Urbina Guerrero
Grupo I-M 1-2 104
Matricula 2530158
"""
# 1_FULL NAME FORMATER:
"""
    Dado el nombre completo de una persona en una sola cadena (por ejemplo: "juan carlos tovar"), el programa debe:
    1) Normalizar el texto (strip, espacios extra, mayúsculas/minúsculas).
    2) Mostrar el nombre formateado en Title Case y las iniciales (por ejemplo: J.C.T.).

    Entradas:
    - full_name (string; nombre completo, puede venir en mayúsculas, minúsculas o mezclado, con espacios extra).

    Salidas:
    - "Formatted name: <Name In Title Case>"
    - "Initials: <X.X.X.>"
"""
try:
    first_name = input("Enter your name: ")
    last_name = input("Enter your last name: ")
    last_name_2 = input("Enter your second last name: ")


    if first_name.isdigit() or last_name.isdigit() or last_name_2.isdigit  :

        print("An error occurred")
        
    else:
        
        Full_name = f"{first_name.strip()} {last_name.strip()} {last_name_2.strip()}"
        print(Full_name.title())

        # Initials of a person:
        initials = f"{first_name[0].strip()}_{last_name[0].strip()}_{last_name_2[0].strip()}"
        print(initials.upper())
except ValueError:
    print("Try again please:)")

"""
    Validaciones:
    - full_name no debe estar vacío después de strip().
    - Debe contener al menos dos palabras (por ejemplo, nombre y apellido).
    - No aceptar cadenas que sean solo espacios.
"""

    ## 2_Email generator:
"""
    Valida si una dirección de correo tiene un formato básico correcto:
    - Contiene exactamente un '@'.
    - Después del '@' debe haber al menos un '.'.
    - No contiene espacios en blanco.
    Si el correo es válido, también muestra el dominio (la parte después de '@').

    Entradas:
    - email_text (string).

    Salidas:
    - "Valid email: true" o "Valid email: false"
    - Si es válido: "Domain: <domain_part>"
"""
email = str(input("Set your email"))
if '@' in email and "." in email and ' ' not in email :
    if email.count("@") == 1:
        print('your email is correct')
    else:
        print('your email is incorrect')
else:
    print('your email is incorrect')

"""
    Validaciones:
    - email_text no vacío tras strip().
    - Contar cuántas veces aparece '@'.
    - Verificar que no haya espacios (no debe haber " " en email_text).
"""
# 3 Palindrome checker:
"""
    Determina si una frase es un palíndromo, es decir, se lee igual de izquierda a derecha y de derecha a izquierda, ignorando espacios y mayúsculas/minúsculas.

    Ejemplos:
    - "Anita lava la tina" -> palíndromo.
    - "Hola mundo" -> no palíndromo.

    Entradas:
    - phrase (string).

    Salidas:
    - "Is palindrome: true" o "Is palindrome: false"
    - (Opcional) Mostrar también la versión normalizada de la frase.
"""
while True:

    print("\n Welcome to the palindrome checker program")
    print("\n You can 'exit' to leave the program")
    word = input("\n\t Enter your word: ")
    if word.strip().lower() == "exit":
        break
    try:
        
    
        if word.isdigit():
                print("\nYour word is not valid,try again")
                continue
        else:
            if word.strip().lower() == word.strip().lower()[::-1]:
                print(f"\nThe word {word} is a palanindrome")
                print(word.strip()[::-1].lower())
                break
            else:
                print(f"\nThe word {word} is not a palanindrome")
                continue

    except ValueError:
    
        print("Your word is not valid, try again")
    except KeyboardInterrupt:
        print("\n Program terminated by the user")
        break
"""
Validaciones:
- phrase no vacía tras strip().
- Longitud mínima razonable después de limpiar 
espacios (por ejemplo, al menos 3 caracteres).
"""
# 4 Sentence word stats
"""
Dada una oración, el programa debe:
1) Normalizar espacios (quitar espacios al principio y al final).
2) Separar las palabras por espacios.
3) Mostrar:
   - Número total de palabras.
   - Primera palabra.
   - Última palabra.
   - Palabra más corta y más larga (por longitud).

Entradas:
- sentence (string).

Salidas:
- "Word count: <n>"
- "First word: <...>"
- "Last word: <...>"
- "Shortest word: <...>"
- "Longest word: <...>"
"""
while True:
    print("\n Welcome to the sentence word stats program")
    print("\n You can 'exit' to leave the program")
    sentence = input("Insert your sentence: ") 

    if sentence == 'exit':
        break
    try:
        if sentence.isdigit() or sentence.isalnum():
            print("An error ocurred;try again please")
            continue
        else:
                print(sentence.strip().split())
                lenght_sentence = len(sentence.strip().split())
                print(f"\nLenght of de sentence: {lenght_sentence}")
                first_word = sentence.strip().split()[0]
                print(f"\nFirst word: {first_word}")
                midle_word = sentence.strip().split()[lenght_sentence // 2]
                print(f"\nMidle word: {midle_word}")
                last_word = sentence.strip().split()[-1]
                print(f"\nLast word: {last_word}")
                short_word = min(sentence.strip().split(), key=len)
                print(f"\nShort word: {short_word}")
                longest_word = max(sentence.strip().split(), key=len)
                print(f"\nLongest word: {longest_word}")
                print(f"\nYour sentence: {sentence}")
                break
            
    except ValueError:
         print("\nAn error ocurred;try again please")
    except KeyboardInterrupt:
        print("\n Program terminated by the user")
        break
"""
Validaciones:
- Oración no vacía tras strip().
- Debe contener al menos una palabra válida después de split().
"""
# 5 Password strength checker:
"""
Clasifica una contraseña como "weak", "medium" o "strong" según reglas mínimas (puedes afinarlas, pero documéntalas en los comentarios).

Ejemplo de reglas:
- Weak: longitud < 8 o todo en minúsculas o muy simple.
- Medium: longitud >= 8 y mezcla de letras (mayúsculas/minúsculas) o dígitos.
- Strong: longitud >= 8 y contiene al menos:
  - una letra mayúscula,
  - una letra minúscula,
  - un dígito,
  - un símbolo no alfanumérico (por ejemplo, !, @, #, etc.).

Entradas:
- password_input (string).

Salidas:
- "Password strength: weak"
- "Password strength: medium"
- "Password strength: strong"
"""
while True:
     print("\n Welcome to the password strength checker program")
     print("\n You can 'exit' to leave the program")
     password = input("Insert your password: ")    
     if password == 'exit':
        break
     try:
        if len(password) < 8 and password.islower or password.isalpha():
            print(f"\n Your password {password} is weak,not strongh,try again please")

        elif len(password) >= 8 and (password.islower() or password.isupper() or password.isdigit()):
            print("\n Your password is medium strength,try again please")

        elif len(password) >= 8 and (password.islower() or password.isupper() or password.isalnum()):
            print(f"\n Your password:{password} is strong")
            print(f"\n Password {password} lenght is {len(password)}")
            break

        else:
            print("\n Your password is not valid,try again please")

     except ValueError:
            print("\nAn error ocurred;try again please")
     except KeyboardInterrupt:
            print("\n Program terminated by the user")
            break
"""
Validaciones:
- No aceptar contraseña vacía.
- Verificar longitud con len().
"""
# 6 Product label formatter:
"""
Dado el nombre de un producto y su precio, genera una etiqueta en una sola línea con el siguiente formato:

Product: <NAME> | Price: $<PRICE>

La cadena completa debe tener exactamente 30 caracteres:
- Si es más corta, rellena con espacios al final.
- Si es más larga, recorta hasta 30 caracteres.

Entradas:
- product_name (string).
- price_value (puede leerse como string o número; conviértelo a string para mostrarlo).

Salidas:
- "Label: <exactly 30 characters>"
(Puedes mostrar la etiqueta entre comillas para que se vean los espacios.)
"""

while True:
     print("\n Welcome to the product label formatter program")
     print("\n You can 'exit' to leave the program")
     product_name = input("\n Insert your product name:" )
     price_value = input("\n Insert your price 'MXN $'")
     if product_name == 'exit':
        break
     try:
            if product_name.isdigit() or product_name == "":
                print("An error ocurred;please try again")
            else:
                print(len((product_name[0:30])))
                label =f"{product_name} costs:{price_value} MXN$"
                print(label)
                print(f"Congratulations your product '{label}' is valid") 
                print(len(label))
                break
     except ValueError:
        print("An error ocurred;please try again")
     except KeyboardInterrupt:
        print("\n Program terminated by the user")
        break

"""
Validaciones:
- product_name no vacío tras strip().
- price_value debe poder convertirse a un número positivo.
"""
"""
    Conclusiones: Los diferentes metodos y built_int de strings
    que exiten nos ayudan a ser mas legible nuestro codigo para 
    los usuarios y simplificar nuestro codigo.

"""
"""
    Referens: https://ellibrodepython.com/python-pep8
    https://javascript.info/coding-style
    https://www.codecademy.com/

"""