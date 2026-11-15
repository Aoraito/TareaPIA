
def lista_enteros(lista):
    resultado = []

    for num in lista:
        if num >= 0 and num not in resultado:
            resultado.append(num)

    resultado.sort()

    return resultado


numeros = [4, -1, 2, 4, 3, -5, 2]

print(lista_enteros(numeros))
