"""
crear una funcion que haciendo uso del metodo filter me filtre los numeros primos de una lista pasada por parametros
"""
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def filtrar_primos(lista):
    return list(filter(es_primo, lista))

# Ejemplo de uso:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primos = filtrar_primos(numeros)
print("Números primos en la lista:", primos)
