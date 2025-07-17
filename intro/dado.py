import random

dado= random.randint(1,6)
intento = input("Introduce un numero:")
if intento == dado:
    print("Le achuntaste")
else:
    print("Intenta otra vez")