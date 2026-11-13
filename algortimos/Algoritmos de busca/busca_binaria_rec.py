def busca_binaria_rec(lista, alvo, ini=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if ini > fim:
        return -1
    meio = (ini + fim) // 2
    print("Meio:", meio)
    if lista[meio] == alvo:
        return meio
    elif lista[meio] < alvo:
        return busca_binaria_rec(lista, alvo, meio + 1, fim)
    else:
        return busca_binaria_rec(lista, alvo, ini, meio - 1)

v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = 9

result = busca_binaria_rec(v,a)

if result == -1:
    print("O alvo não está na lista")
else:
    print("A posição do número que foi buscado na lista é", result)