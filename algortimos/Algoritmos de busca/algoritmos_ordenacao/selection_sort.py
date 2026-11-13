def comb_sort(lista):
    gap = len(lista)
    trocou = True
    while gap > 1 or trocou:
        gap = max(1, int(gap / 1.3))
        trocou = False
        for i in range(len(lista) - gap):
            if lista[i] > lista[i + gap]:
                lista[i], lista[i + gap] = lista[i + gap], lista[i]
                trocou = True
    return lista

lista = [5, 1, 4, 2, 8]
print(comb_sort(lista))