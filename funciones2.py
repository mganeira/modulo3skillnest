"""
def imprimir_numeros_0_n(n=100):
    for i in range(n+1):
        print(i)

imprimir_numeros_0_n()

def imprimir_multiplos_2(inicio, fin):
    for i in range(inicio, fin, 2):
        print(i)
    
imprimir_multiplos_2(0, 500)

def vanilla_ice(n):
    for i in range(n):
        if i % 10 == 0:
            print("ice ice")
        elif i % 5 == 0:
            print("vanilla ice")
        else:
            print(i)

vanilla_ice(100)

def suma_pares_500k(n=50):
    incremento = 0 
    for i in range(0, n+1, 2):
        incremento += i
        print(f"La suma total de los múltiplos de 2 es: {incremento}")

suma_pares_500k()
"""

def cuenta_regresiva_3(n=30):
    for i in range(n, 0, -3):
        print(i)

cuenta_regresiva_3()

def contador_dinamico():
    pass

