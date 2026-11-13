def particiona(lista, baixo, alto):
    pivo = lista[alto]
    i = baixo - 1
    for j in range(baixo, alto):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i+1], lista[alto] = lista[alto], lista[i+1]
    return i + 1
 
def quick_sort(lista, baixo=0, alto=None):
    if alto is None:
        alto = len(lista) - 1
    if baixo < alto:
        p = particiona(lista, baixo, alto)
        quick_sort(lista, baixo, p - 1)
        quick_sort(lista, p + 1, alto)
    return lista

l = [5,1,4,2,8]
print(quick_sort(l))