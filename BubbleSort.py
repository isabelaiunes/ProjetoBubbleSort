# Inicie #
# Loop1: Para cada elemento i no array de tamanho n #
# Loop2: (compara os elementos de novo) Para cada elemento j no array de tamanho n-1 #
# Condicional: Se cada elemento i for maior que elemento j, troque os elementos i e j #
# Exiba o array ordenado #
# Fim #

# Considere esta lista como exemplo para ordenação com Bubble Sort
lista = [6, 3, 12, 7]
# Na primeira vez que o algoritmo passa, se compara elemento i e j e coloca o menor em primeiro lugar #
lista = [3, 6, 12, 7]
# Na segunda vez, se compara o 6 e 12 e não os troca de lugar, pois 6 < 12 #
lista = [3, 6, 12, 7]
# Na terceira vez, o algoritmo compara 12 e 7 e os troca de lugar, porque 7 < 12 #
lista = [3, 6, 7, 12]
