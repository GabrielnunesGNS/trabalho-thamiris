def cocktail_sort(lista):

    inicio, fim = 0, len(lista) - 1
    trocou = True

    while trocou:

        trocou = False

        for i in range(inicio, fim):

            if lista[i] > lista[i + 1]:

                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                trocou = True

        if not trocou:
            break

        fim -= 1
        trocou = False

        for i in range(fim, inicio, -1):

            if lista[i] < lista[i - 1]:

                lista[i], lista[i - 1] = lista[i - 1], lista[i]
                trocou = True

        inicio += 1

    return lista 

lista = [5, 1, 4, 2, 8]
print(cocktail_sort(lista))