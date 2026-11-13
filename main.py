import pandas as pd
from time import perf_counter
import statistics
import csv
import os

# Exemplo de leitura do arquivo:
PATH = 'base_de_dados/base_10000.csv'
dadosCsv = pd.read_csv(PATH, sep=';')#leitura dos dados
lista = dadosCsv.to_dict(orient="records")

def busca_linear(lista,coluna,chave):
    tipo = 'busca linear'
    base = len(lista)
    comparacoes = 0 
    for i in range(len(lista)):
        comparacoes += 1
        if lista[i][coluna] == chave:
            return {
                'funcao':tipo,
                'tamanho lista':base,
                'posicao':i+2,
                'comparacoes':comparacoes
            }
    return -1

def busca_linear_rec(lista,coluna, chave, i=0,comparacoes=0):
    comparacoes = comparacoes
    tipo = 'busca linear rec'
    base = len(lista)
    if i >= len(lista):
        return -1
    if lista[i][coluna] == chave:
                return {
                    'funcao':tipo,
                    'tamanho lista':base,
                    'posicao':i+2,
                    'comparacoes':comparacoes
                }
    return busca_linear_rec(lista,coluna,chave, i + 1,comparacoes + 1)

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
    return lista

def busca_binaria(lista, chave):
    lista = bubble_sort(lista)
    ini, fim = 0, len(lista) - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        if lista[meio] == chave:
            return meio
        elif lista[meio] < chave:
            ini = meio + 1
        else:
            fim = meio - 1
    return -1

def busca_binaria_rec(lista, alvo, ini=0, fim=None):
    lista = bubble_sort(lista)
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

def teste_func_un(funcao, *args):
    inicio = perf_counter()
    resultado = funcao(*args)
    fim = perf_counter()
    return {'resultado':resultado, 
            'tempo fim':fim - inicio,
            }

def teste_func_mul(funcao,*args):
    repeticoes = int(input('insira a quantidade de vezes que o teste irá repetir:\n'))
    tempos = []
    resultado = ''
    for _ in range(repeticoes):
        inicio = perf_counter()
        resultado = funcao(*args)
        fim = perf_counter()
        tempos.append(fim - inicio)
        print
    return {'resultado':resultado, 
            'tempo fim':tempos,
            'repeticoes':repeticoes
            }

def resumir_tempos(tempos):
    return {
        "media": statistics.mean(tempos),
        "mediana": statistics.median(tempos),
        "desvio_padrao": statistics.stdev(tempos) if len(tempos) > 1 else 0
    }

def salvar_resultados_csv(resultados, caminho):
    if not resultados:
        return
    
    # Garante que a pasta onde o arquivo vai ficar existe
    pasta = os.path.dirname(caminho)
    if pasta and not os.path.exists(pasta):
        os.makedirs(pasta)
        
    # Verifica se o arquivo já existe e tem conteúdo
    arquivo_existe = os.path.exists(caminho) and os.path.getsize(caminho) > 0

    # Mudamos de "w" para "a" (append)
    with open(caminho, "a", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=resultados[0].keys())
        
        # Só escreve o cabeçalho se o arquivo ainda não existir
        if not arquivo_existe:
            escritor.writeheader()
            
        escritor.writerows(resultados)
        
    return 1

def salvar(data,caminho):
    resultados = []
    # Extrai os dados do dicionário passado por parâmetro    
    dados = data['resultado']
    
    resultados.append({
        "algoritmo": dados['funcao'],
        "tamanho_base": dados['tamanho lista'],
        "cenario": dados['posicao'],
        "comparacoes": dados['comparacoes'],
        "tempo_medio": data['tempo fim']
    })
    
    
    print('salvando arquivo...')
    if salvar_resultados_csv(resultados, caminho):
        print('arquivo salvo com sucesso!')


def ambiente_teste(funcao,*args):
    caminhoResultados = 'dadosSalvos/resultados.csv'
    caminhoMedias = 'dadosSalvos/media.csv'

    while True:
        try:
            opcao = int(input(
                'Como deseja executar a função?\n'
                '1 - Único\n'
                '2 - Recursivo\n'
                'Opção: '
            ))

            if opcao not in (1, 2):
                print('Opção inválida! Digite 1 ou 2.')
                continue

            break

        except ValueError:
            print('Digite apenas números.')

    # Executa a função escolhida
    if opcao == 1:
        data = teste_func_un(funcao, *args)
    else:
        data = teste_func_mul(funcao, *args)

    # Salva os resultados individuais
    salvar(data, caminhoResultados)

    # Calcula e salva as médias, caso existam repetições
    if 'repeticoes' in data:
        tempos = resumir_tempos(data['tempo fim'])

        dadosMedias = data.copy()
        dadosMedias['tempo fim'] = tempos

        salvar(dadosMedias, caminhoMedias)

    print('Teste finalizado!')


def inicio(lista):
    bdLista = lista 
    print('inicio')
    
    while True:
        try:
            opcao = int(input(
                'Qual função deseja executar?\n'
                '1 - busca linear\n'
                '2 - busca binária\n'
                'Opção: '
            ))

            if opcao not in (1, 2):
                print('Opção inválida! Digite 1 ou 2.')
                continue

            break

        except ValueError:
            print('Digite apenas números.')
    
    if opcao == 1:
        funcao = busca_linear
    else:
        funcao = busca_binaria
    

    
    
    chave = str(input('insita nome para busca \n'))# inserir o nome da busca para roda o teste
    coluna = 'nome' #coluna que sera localizado o registro
    
    
    
    
    
    ambiente_teste(funcao,bdLista,coluna,chave)

inicio(lista)

