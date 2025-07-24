""" 
Programa comparación de zapatillas
alta calidad, calidad media, baja calidad

factores: 
material: cuero, tela, sintético
precio: >100.000, 50.000 - 100.000, < 50.000
tiempo de garantia: mayor a un año, 1 año, menos de 1 año o sin garantia

1 if, 1 elif, else



precio = 0 
material = "cuero" 
garantia = 1
def calcular_calidad(precio, material, garantia):
    precio= int(input("¿Cuánto valen las zapatillas?"))
    material= str(input("¿De qué material son las zapatillas?"))
    garantia= int(input("¿Cuánto tiempo de garantía en años tienen las zapatillas?"))
    if precio > 100000 and (material == "cuero" or "Cuero") and garantia > 1:
        print("Las zapatillas son de alta calidad.")
    elif precio > 100000 and (material == "cuero" or "Cuero") and garantia < 1:
        print("Las zapatillas son de alta calidad.")
    elif precio > 50000 < 100000 and (material == "cuero" or "Cuero") and garantia < 1:
        print("Las zapatillas son de alta calidad.")
        
    if precio > 50000 < 100000 and (material == "tela" or "Tela") and garantia == 1:
        print("Las zapatillas son de calidad media.")

    elif precio > 50000 < 100000 and (material == "tela" or "Tela") and garantia > 1:
        print("Las zapatillas son de calidad media.")

    if precio < 50000 and (material == "sintético" or "Sintético" or "sintética" or "sintetica" or "Sintetica") and garantia < 1:
        print("Las zapatillas son de calidad baja.")
    elif precio < 50000 and (material == "cuero" or "Cuero") and garantia == 1:
        print("Las zapatillas son de calidad alta.")
    elif precio < 50000 and (material == "sintético" or "Sintético" or "sintética" or "sintetica" or "Sintetica") and garantia > 1:
        print("Las zapatillas son de calidad baja.")

    else:
        "No sé la calidad de las zapatillas"



calcular_calidad(precio, material, garantia)

"""

#SOLUCIÓN DEL PROFE

material= input("Material (cuero/tela/sintético):").lower ()

precio= float(input("Precio ($):"))

garantia= int(input("Garantía (años):"))

if material == "cuero" and precio > 100000 and garantia >= 1 :
    print("Alta calidad: Excelentes materiales, durabilidad y confianza.")
elif (material =="tela" and precio >= 50000) or (garantia >=1):
    print("Calidad media: Al menos dos criterios.")

else:
    print("Baja calidad: No cumple con los estándares mínimos.")