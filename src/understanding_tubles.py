"""
    Las tuplas en Python son estructuras de datos inmutables 
    que permiten almacenar múltiples elementos en una sola variable. 
    A diferencia de las listas, las tuplas no pueden ser modificadas 
    después de su creación, lo que las hace ideales 
    para almacenar datos que no deben cambiar.

    Se utilizan las () para definir una tupla, y los elementos 
    dentro de la tupla están separados por comas.

    Ejemplo de creación de una tupla:

"""

#Rectangulo (largo, ancho)
rectangule_dimensions = (200, 50) # tupla
print(f"largo:, {rectangule_dimensions[0]} mm") # 200
print(f"ancho:, {rectangule_dimensions[1]} mm") # 50

#Vamos a intentar modificar un valor de la tupla
# rectangule_dimensions[0] = 250 # Esto generará un error porque 
# las tuplas son inmutables
#rectangule_dimensions[1] = 75 # Esto generará un error porque 
# las tuplas son inmutables

for dimension in rectangule_dimensions :
    print(dimension)

"""
    .No podemos modificar los elementos de una tupla, ni tampoco agregar 
    o eliminar elementos después de su creación.
    lo que si podemos hacer es cambiar la tupla completa 
    por otra tupla nueva.

"""

rectangulo_dimensions = (300, 150, 50) # Nueva tupla