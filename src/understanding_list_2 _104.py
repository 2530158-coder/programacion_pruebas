#Slicing
print("\n Lista de jugadores conn el metodo SLICING")
players = ["CR7", "MESSI", "Travis", 'chicha_god', "corona"]
print(f"\n {players[0:3]}")
#Slice es trbajar con un grupo en especifico
# de elementos de una lista
print(f"\n {players[1:4]}") # ['MESSI', 'Travis', "chicha-god"]
print(f"\n {players[:4]}") # playes = ["CR7", "Travis", "chicha-god"]
print(f"\n {players[:2]}") # players = ["CR7", "MESSI"]

print(f"\n {players[-3:-1]}") # players = ["Travis", 'chicha-god]

Persona = "Edson"
print('Hola soy', Persona, 'y soy puto¡')