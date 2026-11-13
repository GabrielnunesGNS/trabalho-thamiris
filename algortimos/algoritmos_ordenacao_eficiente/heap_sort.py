def heapify(lista, n, i):
    maior = i
    esq, dir = 2 * i + 1, 2 * i + 2
    if esq < n and lista[esq] > lista[maior]:
        maior = esq
    if dir < n and lista[dir] > lista[maior]:
        maior = dir
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior)
 
def heap_sort(lista):
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        heapify(lista, i, 0)
    return lista

l = [5,1,4,2,8]
print(heap_sort(l))