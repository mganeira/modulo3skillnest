"""citas = []
historial = {}
horarios_posibles = ["10:00", "11:00", "12:00", "13:00"]

 "}

def registrar_cita(citas, historial, horarios_posibles):
    nombretutor = input("Ingrese nombre del tutor de la mascota.")
    direcciontutor = input("Ingrese dirección del tutor de la mascota.")
    numerocontacto = int(input("Ingrese un número de contacto."))
    tipodemascota = input("Ingresa qué especie es tu animal.")
    motivovisita = input("Ingresa un motivo por el que traerás a tu mascota")
    datos_tutor.append(nombretutor, direcciontutor, numerocontacto)
    print(datos_tutor)
    print("Tu cita está registrada")

def mostrar_historial():
    print(historial)

while True:
    print("\n--- VetCare ---")
    print("1. Registrar nueva cita")
    print("2. Ver horarios disponibles")
    print("3. Mostrar historial de mascota")
    print("4. Salir\n")
    opcion = input("Seleccione una opción: ")
    if opcion == 1:
        registrar_cita()
    elif opcion == 2:
        print(horarios_posibles)
    elif opcion ==3:
        mostrar_historial()
        pass
    elif opcion == 4:
        print("Saliendo del programa. Adiós.")
        break
    else:
        print("\nOpción inválida.")

"""
#mejorar con la versión del profe