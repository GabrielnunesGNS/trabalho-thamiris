def jump_search(lista, alvo):
    n=len(lista)
    passo = int(n**(1/2))
    print("n:", n, "passo:", passo)

    anterior = 0
    print("valor lista[passo]:", lista[min(passo,n-1)-1])
    while lista[min(passo,n-1)-1]<alvo:
        anterior = passo
        print("anterior:", anterior)
        passo = passo + int(n**(1/2))
        print("passo:", passo)
        if anterior >=n:
            return -1
    
    print("valor lista[anterior]:", lista[anterior])
    while lista[anterior]<alvo:
        anterior = anterior + 1
        print("anterior2:", anterior)
        print("valor lista[anterior]:", lista[anterior])
        if anterior == min(passo,n):
            return -1
        
    if lista[anterior]==alvo:
        return anterior
    return -1

v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = 9

result = jump_search(v, 9)

if result == -1:
    print("O alvo não está na lista")
else:
    print("A posição do número que foi buscado na lista é", result)