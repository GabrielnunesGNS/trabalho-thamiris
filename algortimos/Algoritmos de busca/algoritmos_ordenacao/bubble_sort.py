def bubble_sort(lista):
    n = len(lista)

    comparacoes = 0
    trocas = 0
    passadas = 0

    for i in range(n - 1):
        trocou = False
        passadas += 1

        for j in range(n - 1 - i):
            comparacoes += 1

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

                trocas += 1
                trocou = True

        if not trocou:
            break

    print("Lista ordenada:", lista)
    print("Passadas:", passadas)
    print("Comparações:", comparacoes)
    print("Trocas:", trocas)

    return lista


lista = [5, 1, 4, 2, 8]
bubble_sort(lista)