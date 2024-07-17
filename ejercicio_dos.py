"""
crear una funcion que haciendo uso del metodo filter me filtre los numeros primos de una lista pasada por parametros
"""
def es_primo(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

def filtrar_primos(lista):
    return list(filter(es_primo, lista))

# Ejemplo de uso:
numeros = [23, 4, 17, 10, 29, 31, 16, 5, 7]
primos = filtrar_primos(numeros)
print("Números primos:", primos)
