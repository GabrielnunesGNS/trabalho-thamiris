# Projeto — Laboratório Experimental de Algoritmos com Dados Sintéticos

## Busca, Ordenação, Inserção, Remoção e Análise de Desempenho com Mockaroo

### 1. Contextualização

Em estudos experimentais de algoritmos, bases sintéticas permitem controlar características como tamanho, ordem inicial, distribuição de valores e existência de elementos. Isso possibilita comparar algoritmos em condições equivalentes e observar de forma mais clara o efeito do crescimento da entrada sobre o desempenho.

Neste projeto, os alunos deverão gerar bases sintéticas no **Mockaroo**, implementar algoritmos de busca e ordenação, realizar operações de inserção e remoção e analisar experimentalmente o desempenho dos métodos.

### 2. Objetivo geral

Investigar experimentalmente o comportamento de algoritmos de pesquisa, ordenação e manipulação de dados em bases de diferentes tamanhos e características.

### 3. Objetivos específicos

O aluno deverá ser capaz de:

- gerar conjuntos de dados sintéticos reproduzíveis;
- importar arquivos CSV em Python;
- implementar algoritmos de busca linear e binária;
- implementar versões iterativas e recursivas dos métodos de pesquisa;
- implementar algoritmos de ordenação simples e eficientes;
- implementar inserção e remoção;
- medir tempo de execução e quantidade de comparações;
- analisar a influência do tamanho e do estado inicial dos dados;
- relacionar os resultados experimentais com a complexidade assintótica.

---

## 4. Geração dos dados

Utilize o **Mockaroo** para criar uma base de clientes com, no mínimo, os seguintes campos:

| Campo | Tipo sugerido |
|---|---|
| `id_cliente` | número inteiro único |
| `nome` | nome completo |
| `idade` | inteiro |
| `cidade` | cidade |
| `estado` | estado |
| `data_cadastro` | data |
| `numero_compras` | inteiro |
| `valor_total` | decimal |

O campo `id_cliente` será a chave principal de pesquisa.

---

## 5. Bases obrigatórias

Cada aluno deverá gerar:

- `clientes_1000.csv` — 1.000 registros;
- `clientes_10000.csv` — 10.000 registros;
- `clientes_100000.csv` — 100.000 registros.

Como desafio opcional, poderá ser incluída uma base com 1.000.000 de registros.

Para cada tamanho, prepare duas versões:

### Versão A — desordenada

IDs em ordem aleatória.

### Versão B — ordenada

IDs em ordem crescente.

Exemplo de organização dos arquivos:

```text
base_1000_desordenada.csv
base_1000_ordenada.csv
base_10000_desordenada.csv
base_10000_ordenada.csv
base_100000_desordenada.csv
base_100000_ordenada.csv
```

---

## 6. Algoritmos de pesquisa

Implemente obrigatoriamente:

- busca linear;
- busca linear recursiva;
- busca binária;
- busca binária recursiva.

Como extensão, poderá ser implementada a busca por salto.

Não utilize funções prontas da linguagem para substituir os algoritmos exigidos.

---

## 7. Algoritmos de ordenação

Implemente:

- Bubble Sort;
- Selection Sort;
- Insertion Sort;
- Shell Sort;
- Merge Sort;
- Quick Sort;
- Heap Sort.

Caso um algoritmo simples se torne excessivamente lento nas maiores bases, registre isso como parte do experimento. O professor poderá definir um limite máximo de tempo por execução.

---

## 8. Experimento 1 — Crescimento da base

Execute os algoritmos de pesquisa sobre bases de:

- 1.000 registros;
- 10.000 registros;
- 100.000 registros.

Monte uma tabela comparativa contendo, pelo menos, tempo médio e quantidade de comparações.

---

## 9. Experimento 2 — Posição do elemento

Para cada base, procure elementos situados:

- no início;
- aproximadamente em 25%;
- aproximadamente em 50%;
- aproximadamente em 75%;
- no final;
- fora da base.

Analise o impacto da posição sobre os algoritmos.

---

## 10. Experimento 3 — Número de comparações

Além do tempo de execução, conte quantas comparações cada busca realizou.

Exemplo:

```python
comparacoes = 0
```

A cada comparação relevante:

```python
comparacoes += 1
```

Explique por que o número de comparações pode ser uma medida mais estável para observar a complexidade do algoritmo do que o tempo bruto obtido em um único computador.

---

## 11. Experimento 4 — Crescimento assintótico

Produza um gráfico:

**Número de registros × número de comparações**

para:

- busca linear;
- busca binária.

Compare o comportamento observado com as complexidades esperadas `O(n)` e `O(log n)`.

---

## 12. Experimento 5 — Algoritmos de ordenação

Execute os algoritmos de ordenação sobre diferentes tamanhos de base.

Registre, quando possível:

- tempo de execução;
- número de comparações;
- número de movimentações.

Monte uma tabela comparativa para todos os algoritmos.

---

## 13. Experimento 6 — Influência do estado inicial

Execute os algoritmos de ordenação em três situações:

1. dados aleatórios;
2. dados previamente ordenados;
3. dados em ordem inversa.

Responda:

> O estado inicial da estrutura afeta igualmente todos os algoritmos de ordenação?

---

## 14. Experimento 7 — Inserção

Em uma estrutura ordenada, insira elementos em diferentes regiões:

- início;
- aproximadamente 25%;
- meio;
- aproximadamente 75%;
- final.

Compare duas estratégias:

### Estratégia A

Inserir ao final e ordenar novamente toda a estrutura.

### Estratégia B

Localizar a posição correta e inserir mantendo a estrutura ordenada.

Registre o tempo de ambas.

---

## 15. Experimento 8 — Remoção

Remova elementos localizados:

- no início;
- no meio;
- no final.

Registre:

- tempo de localização;
- tempo de remoção;
- tempo total.

---

## 16. Experimento 9 — Muitas consultas

Considere uma base com **100.000 registros**.

Compare:

### Sistema A

Dados desordenados + `N` buscas lineares.

### Sistema B

Dados desordenados + um algoritmo eficiente de ordenação + `N` buscas binárias.

Execute para:

- 1 busca;
- 10 buscas;
- 100 buscas;
- 1.000 buscas;
- 10.000 buscas.

O aluno deverá determinar experimentalmente quando o custo inicial da ordenação começa a ser compensado pela redução no tempo das buscas seguintes.

---

## 17. Metodologia de medição

Recomenda-se executar cada cenário **30 vezes**.

Calcule, no mínimo:

- média;
- mediana;
- desvio padrão.

Utilize preferencialmente:

```python
from time import perf_counter
```

No relatório, descreva também:

- processador;
- memória RAM;
- sistema operacional;
- versão do Python;
- ambiente de desenvolvimento utilizado.

---

## 18. Pergunta central do projeto

O relatório deverá responder:

> Existe um algoritmo universalmente mais eficiente para pesquisar, ordenar e manipular dados?

A resposta deverá considerar:

- tamanho dos dados;
- estado inicial da estrutura;
- frequência das consultas;
- frequência das inserções;
- frequência das remoções;
- custo da ordenação;
- número de comparações;
- uso de memória;
- tempo total do sistema.

---

## 19. Gráficos obrigatórios

O relatório deverá apresentar pelo menos:

1. **Número de registros × tempo de busca**;
2. **Número de registros × número de comparações**;
3. **Número de registros × tempo de ordenação**;
4. **Quantidade de buscas × tempo total do sistema**;
5. um gráfico adicional escolhido pelo aluno para sustentar uma conclusão relevante.

---

## 20. Entregáveis

| Arquivo | Conteúdo |
|---|---|
| Código-fonte | implementação completa dos algoritmos |
| Resultados em CSV | métricas coletadas nos experimentos |
| Gráficos | visualizações utilizadas na análise |
| README | instruções de execução |
| Relatório em PDF | análise completa utilizando o template em LaTeX fornecido |

---

## 21. Estrutura do relatório

1. Introdução;
2. Base de dados;
3. Algoritmos implementados;
4. Metodologia experimental;
5. Resultados;
6. Análise e discussão;
7. Conclusão;
8. Referências;
9. Apêndices, se necessário.

---

## 22. Critérios de avaliação

| Critério | Peso |
|---|---:|
| Implementação correta dos algoritmos | 20% |
| Planejamento experimental | 20% |
| Coleta e tratamento dos tempos | 15% |
| Comparação das complexidades | 15% |
| Gráficos e resultados | 10% |
| Discussão crítica | 15% |
| Organização e qualidade do código | 5% |

### Observação final

O objetivo do projeto não é apenas identificar o algoritmo mais rápido em uma execução isolada, mas compreender **em quais condições cada estratégia é mais adequada**.
