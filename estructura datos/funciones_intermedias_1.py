# A. Actualizar valores en diccionarios y listas

matriz = [ [10, 15, 20], [3, 7, 14] ]

matriz[0][2] = 6
print(matriz)

cantantes1 = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]


cantantes1[0]["nombre"] = "Enrique Martin Morales"
print(cantantes1)

ciudades = {
   "México": ["Ciudad de México", "Guadalajara", "Cancún"],
   "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

ciudades["México"][2] = "Monterrey"
print(ciudades)


coordenadas = [ {"latitud": 8.2588997, "longitud": -84.9399704}

]

coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)


cantantes2 = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "México"},

   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]
#B.

#2. Iterar a través de una lista de diccionarios Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios 
# y recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente. Por ejemplo:


def iterarDiccionario(lista):
    for diccionario in lista:
        for llave, valor in diccionario.items():
            print(f"Nombre: {llave}, país: {valor}")

iterarDiccionario(cantantes2)

#3. Crea la función iterarDiccionario2(llave, lista) que reciba una cadena con el nombre de una llave y una lista de diccionarios. 
# La función debe imprimir el valor almacenado para esa clave de cada diccionario que se encuentra en la lista. 


def iterarDiccionario2(llave, lista):
  for diccionario in lista:
    if llave in diccionario:
      print(diccionario[llave])
    else:
      print(f"La llave '{llave}' no existe.")

iterarDiccionario2("nombre",cantantes2)

#4. Iterar a través de un diccionario con valores de lista Crea una función imprimirInformacion(diccionario) que reciba un diccionario en donde los valores son listas. La función debe
#imprimir el nombre de cada clave junto con el tamaño de su lista y seguido de esto los valores de la lista para esa clave.

costa_rica = {

   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]

}



def imprimirInformacion(diccionario):
 for lista in diccionario:
    for clave, valor in diccionario.items():
        print(len(valor), clave.upper())
        for i in valor:
                print(i)

imprimirInformacion(costa_rica)