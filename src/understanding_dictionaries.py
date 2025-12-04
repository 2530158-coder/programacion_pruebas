# Dictionaries

alien_0 = {'color': 'green', 'points': 5}

# The simpliest dictionary

alien_1 = {'color': 'yellow'}

# Accesing values in a dictionary
print(alien_1['color'])
print(alien_0['points'])

# Empty dictionary
alien_2 = {}

# Modifiyng values in a dictionary
alien_2 = {'color': 'yellow'}
alien_2 ['color'] = 'blue'


# Adding new key-value pairs
alien_2['x_position'] = 0
alien_2['y_position'] = 25

print(alien_2)

# Dictionary with similar objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# Looping through all key-value pairs
for key, value in favorite_languages.items():
    print(f"{key.title()}'s favorite \
language is {value.title()}.")
# Looping through all keys

# Looping through all keys and values separately 
for key in favorite_languages.keys():
    print(key.title())

# Looping through all values
for value in favorite_languages.values():
    print(value.title())

# Nesting dictionaries

# Dictionary inside a dictionary

# Listas de diccionarios
covenant_grunt = {
    "color": "blue",
    "weapon": "plasma rifle",
    "armament": "energy sword",

    }

covenant_elite = {
    "color": "red",
    "weapon": "plasma rifle",
    "armament": "energy sword",
    }

covenant_jackal = {
    "color": "yellow",
    "weapon": "plasma pistol",
    "armament": "energy sword",
    }

# Lista de diccionarios
covenants  = [
    covenant_grunt, 
    covenant_elite, 
    covenant_jackal
    ]

for covenant in covenants:
    print("\n",covenant)
    for key, value in covenant.items():
        print(f"{key}: {value}")
    print("\n")


# Listas en diccionarios
students = {
    "jorge": ["reprobado", "aprobado", " toreto"],
    "gerardo": ["aprobado", "cbti271", "migajero"]

}
