
precio_pantalon= 4599
precio_calzado= 7999

descuento_ropa= 20
descuento_calzado= 15

precio_final_ropa= round(4599 * (1 - 20 / 100))
precio_final_calzado = round(7999 * (1 - 15 / 100))
ahorro_ropa= precio_pantalon - precio_final_ropa
ahorro_calzado=precio_calzado - precio_final_calzado
print(f"La ropa cuesta ahora {precio_final_ropa}, ahorro {ahorro_ropa}")
print(f"El calzado cuesta ahora {precio_final_calzado}, ahorro {ahorro_calzado}")
