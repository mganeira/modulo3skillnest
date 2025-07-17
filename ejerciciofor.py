"""ciudades_principales= ["Temuco", "Lautaro"]
for ciudad in ciudades_principales:
    print(ciudad)


for ciudad in enumerate(ciudades_principales):
    print(f"Ciudad en el índice: {ciudad}")

"""

santiago = {
    "nombre": "Santiago", 
    "region": "Metropolitana", 
    "poblacion": 5_614_000, 
    "altitud": 570,  # metros sobre el nivel del mar
    "fundacion": 1541  # año de fundación
}


for clave in santiago:
    print(clave)

for valor in santiago.values():
    print(valor)

for llave in santiago.keys():
    print(llave)

for llave, valor in santiago.items():
    print(llave, valor)