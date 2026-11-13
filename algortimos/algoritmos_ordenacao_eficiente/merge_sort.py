def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esq = merge_sort(lista[:meio])
    dire = merge_sort(lista[meio:])
    return fundir(esq, dire)
 
def fundir(esq, dire):
    resultado, i, j = [], 0, 0
    while i < len(esq) and j < len(dire):
        if esq[i] <= dire[j]:
            resultado.append(esq[i]); i += 1
        else:
            resultado.append(dire[j]); j += 1
    resultado.extend(esq[i:])
    resultado.extend(dire[j:])
    return resultado

l = [5,1,4,2,8]
print(merge_sort(l))