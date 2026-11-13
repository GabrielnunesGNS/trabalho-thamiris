def busca_linear(lista, alvo):
    for i in range(len(lista)):
        print(v[i])
        if lista[i] == alvo:
            return i
    return -1


v = [2, 3, 4, 6, 1, 5, 8, 9, 10]
a = 0

if busca_linear(v,a) == -1:
    print("O alvo não está na lista")
else:
    print("A posição do número que foi buscado na lista é", busca_linear(v,a))