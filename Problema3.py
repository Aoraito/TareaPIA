def trabajar_conjuntos(lista1, lista2):
    
    lista1_conjunto = set(lista1)
    lista2_conjunto = set(lista2)

    interseccion = lista1_conjunto.intersection(lista2_conjunto)
    union = lista1_conjunto.union(lista2_conjunto)
    diferencia_simetrica = lista1_conjunto.symmetric_difference(lista2_conjunto)

    resultado = {"Interseccion": interseccion, "Union": union, "Diferencia simetrica": diferencia_simetrica}

    return  resultado


lista1 = [1, 2, 5]
lista2 = [1, 3, 5, 7]

resultado = trabajar_conjuntos(lista1, lista2)

print(resultado)