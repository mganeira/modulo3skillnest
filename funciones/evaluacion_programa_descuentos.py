"""Objetivo
Crear un programa en Python que determine el descuento aplicado a una compra según los siguientes criterios:
Si el cliente compra más de 10 productos, obtiene un descuento del 10%.
Si el cliente es frecuente (más de 5 compras previas), se aplica un 5% adicional.
Si la compra supera los 500 dólares, se otorga un descuento adicional del 7%.
En días de promoción especial, se aplica un 15% adicional.
Ningún cliente puede obtener un descuento mayor al 30% en total.
Requerimientos
Uso de condicionales: Implementar estructuras if, elif, else para evaluar cada condición.
Subcondiciones: Combinar condiciones dentro de una misma evaluación.
Condiciones de borde: Asegurar que el programa maneje casos como exactamente 10 productos, exactamente 500 dólares, etc.
Condiciones anidadas: Evaluar casos donde varias condiciones sean verdaderas al mismo tiempo.
Salida controlada: Si ninguna condición se cumple, el descuento será 0%.
Convención de nombres: Utilizar snake_case en todas las variables y funciones.
Diagrama de flujo: Dibujar un diagrama que represente la lógica del programa antes de implementarlo.
"""

unidades = int(input("¿Cuántas unidades del producto vas a comprar?  "))
precio = 98 
cliente_frecuente = bool(input("¿Eres cliente frecuente?: "))
precio_original = int(precio * unidades)
dia = input("¿Qué día es hoy?:  ")
descuento_acumulado = 0
precio_final = 0

def compra(unidades, precio_original, descuento_acumulado, precio_final):
    if precio_original > 500:
        descuento_acumulado += 7
        print("Se le hizo un descuento del 7% por compra de alto valor.")
    elif precio_original == 500:
        print("No hay descuento para ti. Gasta más de 500 dólares y tendrás descuento del 7%.")


    if dia == "miercoles" or "Miercoles" or "Miércoles" or "miércoles":
            descuento_acumulado += 15
            print("Tienes un descuento del 15% porque hoy es día miércoles.")
    else:
         print("No hay descuento extra porque hoy no es miércoles.")

    if unidades == 10 :
            print("No hay modificación en el precio. Si quieres descuento, compra más de 10 unidades.")
    elif unidades > 10 :
        descuento_acumulado += 10
        print(f'Tienes un descuento del 10% porque llevas más de 10 uniades.')
    else: 
         print("No hay descuento, llevas menos de 10 unidades.")

    if cliente_frecuente == True and descuento_acumulado < 25 :
        descuento_acumulado += 5
        print("Tienes un descuento del 5% por ser cliente frecuente.")
    else:
        print("No hay descuento para ti.")
    
        precio_final = ( precio_original - ( precio_original * (descuento_acumulado / 100)))

    if descuento_acumulado >= 30:
          print("No se pueden hacer más descuentos, el máximo es 30%.")
          print(f'El precio a pagar es {precio_final}')

(compra(unidades, precio_original, descuento_acumulado, precio_final))

    