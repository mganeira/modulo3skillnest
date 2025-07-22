from pprint import pprint 
#Importamos el módulo para ordenar la lista de diccionarios
#Menú interactivo
# Definición del menú inicial        
menu = """
Gestor de Tareas
---
1. Agregar tarea
2. Ver tareas
3. Marcar tarea como completada
4. Eliminar tarea
5. Salir
"""
#Definición de funciones

#Verificar la tarea

def ingresar_tarea():
    tarea = input("Ingresa la tarea:  ").lower()
    return tarea
#Verificar el número que se ingresa al menú
def verificar_num():  
     while True:
          try:
               opcion = int(input("Ingresa un número del 1 al 5:  "))
               if opcion in range(1,6):
                return opcion
               else:
                   print("Da un número del 1 al 5:   ")
          except ValueError:
              print("Escribe un número válido.")
            
#Verificar el número que se ingresa a estado
            
def verificar_estado():
     while True:
          try:
               estado = int(input("Ingresa un 1 si la tarea está pendiente o 2 si está completa:  "))
               if estado in range(1,3):
                return estado
               else:
                   print("Solo 1 o 2.")
          except ValueError:
              print("Escribe un número válido.")
    
#Definición de función agregar tarea

def agregar_tarea(lista):
     print("Vamos a crear una tarea.")
     tarea = ingresar_tarea()
     if tarea not in lista:
      estado = verificar_estado()
      if estado == 1:
        cosa= {"tarea": tarea, "estado": "pendiente"}    
        lista.append(cosa)
        print(f"Tarea añadida: {cosa}") 
      else:
        cosa= {"tarea": tarea, "estado": "completa"}        
        lista.append(cosa)
        print(f"Tarea añadida: {cosa}")
     else:
        print("La tarea ya existe en la lista.")

#Definición de función completar tarea
def completar_tarea(lista):
        if len(lista) == 0:
            print("No hay tareas en la lista.")
        else:
          print("¿Qué tarea quieres completar?")
          tarea = ingresar_tarea()
          contador = 0
          for diccionario in lista :
              if tarea == diccionario["tarea"]:
                if diccionario["estado"] == "completa":
                    contador =+ 2 
                else:
                    diccionario["estado"] = "completa"
                    contador =+ 1
          if contador == 0:
              print("No existe esta tarea. Por favor, ve la lista de tareas y escoge una existente.")
          elif contador == 2:
              print("La tarea ya está completa.")
          else:
              print(f"El estado de tu tarea {tarea} ha sido cambiado. ")
              
#Definición de función eliminar tarea              
def eliminar_tarea(lista):
        if len(lista) == 0:
            print("No hay tareas en la lista.")
        else:
         print("¿Qué tarea quieres eliminar?")
         tarea = ingresar_tarea()
         contador = 0
         for diccionario in lista:
          if tarea == diccionario["tarea"]:
            lista.remove(diccionario)
            contador += 1
            if contador == 0:
                print("No existe esta tarea. Por favor, ve la lista de tareas y escoge una existente.")
            else:
                print(f"Tu tarea {tarea} ha sido eliminada. ")
              

#Definir función para verificar cuando se añada tarea

def listar_tareas(lista):
    if len(lista) > 0:
        pprint(lista)
    else:
      print("No hay tareas.")

#Definición del programa central

def gestor_tarea(texto):
      tareas = []
      while True:
        print(texto)
        opcion = verificar_num()

        if opcion == 1:
          agregar_tarea(tareas)
          
        elif opcion == 2:
            listar_tareas(tareas)

        elif opcion == 3:
            completar_tarea(tareas)

        elif opcion == 4:
          eliminar_tarea(tareas)

        else:
          print("Adiós uwu.")
          break
#Se llama al programa

gestor_tarea(menu)
