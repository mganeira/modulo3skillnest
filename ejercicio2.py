#Ganancias y costos
#fruteria

#Precio de venta

preciokmzn= 950
precioknrj= 1300

costocommanz= 600 * 10
costocomnrj= 850 *15

ventamzn= 10
ventanrj = 15
costofijo= 5000
gananciasbrutas = costocommanz + costocomnrj
gananciasmanzanas= ventamzn * preciokmzn
ganancianaranjas = ventanrj * precioknrj
gananciasnetas = gananciasmanzanas + ganancianaranjas - gananciasbrutas - costofijo
print(f"Las ganancias netas son {gananciasnetas}")