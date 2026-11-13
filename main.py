import pandas as pd
from time import perf_counter
import statistics
import csv
import os

# Exemplo de leitura do arquivo:


def busca_linear(lista,coluna,chave):
    tipo = 'busca linear'
    base = len(lista)
    comparacoes = 0 
    for i in range(len(lista)):
        comparacoes += 1
        if lista[i][coluna] == chave:
            return {
                'funcao':tipo,
                'chave':chave,
                'tamanho lista':base,
                'posicao':i+2,
                'comparacoes':comparacoes
            }
    return {
        'funcao':tipo,
        'chave':chave,
        'tamanho lista':base,
        'posicao':'não encontrado',
        'comparacoes':comparacoes
    }

def busca_linear_rec(lista,coluna, chave, i=0,comparacoes=0):
    comparacoes = comparacoes
    tipo = 'busca linear rec'
    base = len(lista)
    if i >= len(lista):
        return {
                'funcao':tipo,
                'chave':chave,
                'tamanho lista':base,
                'posicao':'não encontrado',
                'comparacoes':comparacoes
            }
    if lista[i][coluna] == chave:
                return {
                    'funcao':tipo,
                    'chave':chave,
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

            # Compara os IDs dos dicionários
            if lista[j]['id'] > lista[j + 1]['id']:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

                trocas += 1
                trocou = True

        if not trocou:
            break

    return lista

def busca_binaria(lista,coluna,chave):
    tipo = 'busca binaria'
    base = len(lista)
    lista = bubble_sort(lista)
    ini, fim = 0, len(lista) - 1
    comparacoes = 0
    while ini <= fim:
        comparacoes += 1
        meio = (ini + fim) // 2
        if lista[meio][coluna] == chave:
            return {
                    'funcao':tipo,
                    'chave':chave,
                    'tamanho lista':base,
                    'posicao':meio,
                    'comparacoes':comparacoes
                }
        elif lista[meio][coluna] < chave:
            ini = meio + 1
        else:
            fim = meio - 1
    return {
            'funcao':tipo,
            'chave':chave,
            'tamanho lista':base,
            'posicao':'não encontrado',
            'comparacoes':comparacoes
        }

def busca_binaria_rec(lista, coluna, chave, ini=0, fim=None, comparacoes=0):

    tipo = 'busca binaria rec'
    base = len(lista)

    if fim is None:
        fim = len(lista) - 1

    if ini > fim:
        return {
            'funcao': tipo,
            'tamanho lista': base,
            'posicao': -1,
            'comparacoes': comparacoes
        }

    meio = (ini + fim) // 2
    comparacoes += 1

    if lista[meio][coluna] == chave:
        return {
            'funcao': tipo,
            'tamanho lista': base,
            'posicao': meio,
            'comparacoes': comparacoes
        }

    elif lista[meio][coluna] < chave:
        return busca_binaria_rec(
            lista, coluna, chave,
            meio + 1, fim, comparacoes
        )

    else:
        return busca_binaria_rec(
            lista, coluna, chave,
            ini, meio - 1, comparacoes
        )

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
        "alvo":dados['chave'],
        "posicao": dados['posicao'],
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


def inicio():
    
    print('inicio')
    
    while True:
        try:
            path = int(input(
                'Qual base de arquivo deseja executar o ambiente?\n'
                '1 - base 1.000\n'
                '2 - base 10.000\n'
                '3 - base 100.000\n'
                'Opção: '
            ))

            if path not in (1, 2):
                print('Opção inválida! Digite 1 ou 2.')
                continue

            break

        except ValueError:
            print('Digite apenas números.')
    
    if path == 1 :
        arquivo = 'base_de_dados/base1000.csv'
    elif path == 2:
        arquivo = 'base_de_dados/base10000.csv'
    else:  
        arquivo = 'base_de_dados/base1000000.csv' 
    
    
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
    
    #coluna que sera localizado o registros
    chave = int(input('insira o id que deseja localizar:\n')) #chave para ser localizada
    coluna = 'id' #coluna de busca
    lista  = dadosCsv = pd.read_csv(arquivo, sep=';')#leitura dos dados
    lista = dadosCsv.to_dict(orient="records")
    
    
    
    ambiente_teste(funcao,lista,coluna,chave)

inicio()

