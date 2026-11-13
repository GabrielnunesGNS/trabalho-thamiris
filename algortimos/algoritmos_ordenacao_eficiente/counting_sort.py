import time
import random

def counting_sort(lista):
    # Marca o tempo de início
    inicio = time.perf_counter()
    maior = max(lista)
    contagem = [0] * (maior + 1)
    for valor in lista:
        contagem[valor] += 1
    print("Contagem:", contagem)
    resultado = []
    for valor, vezes in enumerate(contagem):
        resultado.extend([valor] * vezes)
    # Marca o tempo de término
    fim = time.perf_counter()
    # Calcula a diferença
    tempo_total = fim - inicio
    print(f"Tempo de execução: {tempo_total:.6f} segundos")
    return resultado

l = [5,1,4,2,8]
print(counting_sort(l))
lista = [7,9,0,10,26,7,9,6,4,5,2,1,1]
print(counting_sort(lista))
numeros_desordenados = [
    45, 12, 89, 3, 23, 78, 56, 91, 34, 12, 7, 88, 43, 21, 65, 
    99, 2, 11, 76, 54, 33, 22, 10, 87, 68, 49, 39, 29, 19, 81
]
print(counting_sort(numeros_desordenados))

# Define a semente para que o resultado seja sempre o mesmo (opcional)
random.seed(42)

# Gera uma lista com 10.000 números aleatórios entre 1 e 100.000
lista_grande_desordenada = [random.randint(1, 1000) for _ in range(1000)]

# Exibe os 10 primeiros elementos apenas para conferência
print("Primeiros 10 itens:", lista_grande_desordenada[:10])
print("Tamanho total da lista:", len(lista_grande_desordenada))
print(counting_sort(lista_grande_desordenada))