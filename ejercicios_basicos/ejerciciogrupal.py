"""
Solución

Se debe desarrollar un programa en Python que realice las siguientes funciones:

Mostrar la lista de excursiones disponibles con cupos limitados.

Permitir a los usuarios reservar un cupo ingresando su nombre y el número de excursión deseada.

Verificar si hay cupos disponibles antes de confirmar la reserva.

Manejar condiciones como excursiones llenas o intentos inválidos de reserva.

Utilizar ciclos para mostrar y actualizar la información en tiempo real.

Implementar las instrucciones break y continue para controlar el flujo del programa.



"""
reservas = []

cupos_conguillio = 4
cupos_villarica = 4
cupos_pucon = 4
boletos_conguillio = 0 
boletos_villarica = 0 
boletos_pucon = 0 

intro = (f"Bienvenido a EcoViaje. El viaje de hoy es al Parque Conguillio. Por favor ingresa el numero de excursion y tu nombre para agendar visita. ")


while boletos_conguillio < cupos_conguillio and boletos_pucon < cupos_pucon and boletos_villarica < cupos_villarica:
        print(intro)
        nombre = input("Ingresa tu nombre:  ")
        lugar = int(input("0: Parque Conguillio. Cupos disponibles: {cupos_conguillio} 1: Lago Villarica. Cupos disponibles: {cupos_villarica} 2: Playa Pucón. Cupos disponibles: {cupos_pucon}.:    "))
        if lugar == 0:
            boletos_conguillio = int(input("¿Cuántos boletos vas a comprar?:   "))
            cupos_conguillio = cupos_conguillio - boletos_conguillio
            reservas.append(nombre)
            print(f"Reserva realizada. Cupos disponibles para Parque Conguillio ahora son {cupos_conguillio}")    
        elif lugar == 1:
            print(f"El cupo disponible es {cupos_villarica}")
            boletos_villarica = int(input("¿Cuántos boletos vas a comprar?:   "))    
            cupos_conguillio = cupos_conguillio - boletos_villarica
            reservas.append(nombre)
            print(f"Reserva realizada. Cupos disponibles para Villarica ahora son {cupos_villarica}")
        elif lugar == 2:
            boletos_pucon = int(input("¿Cuántos boletos vas a comprar?:   "))    
            cupos_pucon = cupos_pucon - boletos_pucon
            reservas.append(nombre)
            print(f"Reserva realizada. Cupos disponibles para Pucón ahora son {cupos_pucon}")
        if cupos_villarica == 0:
             print("Cupos llenos, no se aceptan más reservas.")
        if cupos_conguillio == 0:
             print("Cupos llenos, no se aceptan más reservas.")
        if cupos_pucon == 0:
             print("Cupos llenos, no se aceptan más reservas.")
        if len(reservas) > 0:
            print(reservas) 
            break


