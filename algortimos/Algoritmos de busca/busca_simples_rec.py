def busca_linear_rec(lista, alvo, i=0):
    if i >= len(lista):
        return -1
    if lista[i] == alvo:
        return i
    print("tamanho da lista: ",len(lista), "numero: ", lista[i])
    return busca_linear_rec(lista, alvo, i + 1)

v = [2, 3, 6, 8, 9, 10, 5, 4, 1]
a = 1

result = busca_linear_rec(v,a, 0)

if result == -1:
    print("O alvo não está na lista")
else:
    print("A posição do número que foi buscado na lista é", result)