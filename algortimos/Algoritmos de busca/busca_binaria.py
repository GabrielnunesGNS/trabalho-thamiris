def busca_binaria(lista, alvo):
    ini, fim = 0, len(lista) - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            ini = meio + 1
        else:
            fim = meio - 1
    return -1

v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = 9

result = busca_binaria(v,a)

if result == -1:
    print("O alvo não está na lista")
else:
    print("A posição do número que foi buscado na lista é", result)