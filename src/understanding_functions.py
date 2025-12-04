"""
    Functions

    Las funciones son bloques de codigo diseñados
    para realizar una tarea especifica.

    Cuando queremos realizar la tarea que se ah definido
    en una funcion, tenemos que llenar 
    el nombre de la funcion responsable de esto.

    Definicion de funciones (Syntaxtis):

    def nombre_de_la_funcion(parametro1, parametro2):
        acciones

"""
def greating_mauro():
    print("Hola Mauro, que gusto verte")
    
#Parametros de la funcion
def great(user_name, ms):
    print(f"Hola {user_name}, {ms} !!!")

#Llamado de la funcion Argumentos
greating_mauro()
great("Edson","Que haces")


# Argumentos
#greating_Mauro

"""
    Vamos a realizar un programa que genere 
    el nombre completo de una pesona.

    Vamos a pasar el primer nombre, el segundo nombre,
    y el apellido como parametros de la funcion.

    La funcion debe de generar el nombre completo
    y retornarlo.

"""
def create_full_name(first_name, last_name, middle_name ' '):
    """
    Docstrings = Jorge this function creates a full name
    of a person given its three names.
    """
    full_name = f"{first_name.strip().title()} {middle_name.strip().title()} {last_name.strip().title()}"
    return full_name .title()

user_first_name = input("Escribe tu primer nombre")
user_middle_name = input("Escribe tu segundo nobre")
user_last_name = input("Escribe tus apellidos")

# Argumentos Posicionales
print(create_full_name(
    user_first_name, 
    user_middle_name, 
    user_last_name))

full_name = create_full_name(
    user_first_name, 
    user_middle_name, 
    user_last_name)

print(full_name)


# Argumentos con palabras clave
full_name_key = create_full_name(
    last_name=user_last_name,
    first_name=user_first_name,
    middle_name=user_middle_name)

print(full_name_key)


# Parametros opcionales
profe_falso = create_full_name(user_name, user_last_name)
print(profe_falso)


# Temas para estudiar a futuro:
# Funciones: args y kwargs
# Funciones de datos: abrir archivos csv; :json, .yml , .txt, .xml
# Argumentos por linea de comandos - sys
# cli - command line interface
# generadores, iteradores, yield
# testing ->

