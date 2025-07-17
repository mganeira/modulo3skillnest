#ARGS

def suma(*numeros):
    print(type(numeros))
    print(f"Argumentos recibidos: {numeros}")
    resultado = sum(numeros)
    return resultado
#KWARGS
def mostrar_info(**datos):
    print(datos)
    print(datos.keys())
    print(datos.values())