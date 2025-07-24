"""combinar condicionales and or if"""

paltas_precio = 3990
cantidad_kilos = 0
suavidad= False
duras= True
tomates_precio: 2000

if paltas_precio < 4990 and duras or tomates_precio < 2500:
    print("Se hacen completos.")
else:
    print("No se hacen completos hoy.")

#Gato negro    
gato_color= "negro"
gato_nombre= "nombre"


if not gato_color == "amarillo" and not gato_nombre != "bagueera" or gato_color == "negro":
    gato_nombre = "bagueera"
    print(f"Su nombre es {gato_nombre}")

