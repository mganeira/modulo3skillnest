#lista1 = [1, 2, 3, 4, 5, 5]
#lista2 = [4, 5, 6, 7, 8]

#set1= set(lista1)
#set2 =set(lista2)
#print(lista1)
#print(lista2)
#print(type(set1))

#union=
# lista 1 | lista 2 

#interseccion: (&)
#4, 5
#print(set1 & set2)
#diferencia:
#1,2,3
#print(set1-set2)
#diferencia simetrica:
#1,2,3,6,7,8
#print(set1 ^ set2)



#EJERCICIO 2 ALIMENTOS

#Alimentos favoritos de un grupo de estudiantes
estudiantes = {"pizza", "hamburguesa", "sushi", "tacos", "ensalada"}
# Alimentos favoritos de un grupo de deportistas
deportistas = {"pollo", "ensalada", "sushi", "batidos", "huevos"}
# 0. Unión de alimentos
union_alimentos= (estudiantes | deportistas)
print(union_alimentos)
# 1. Alimentos comunes en ambos grupos (intersección)
interseccion_alimentos= (estudiantes & deportistas) 
print(interseccion_alimentos)
# 2. Alimentos únicos de los estudiantes (diferencia)
diferencia = estudiantes - deportistas
diferencia2= deportistas  - estudiantes
print(diferencia)
print(diferencia2)
# 3. Alimentos únicos de los deportistas (diferencia)
diferenciasim= diferencia ^ diferencia2
print(diferenciasim)