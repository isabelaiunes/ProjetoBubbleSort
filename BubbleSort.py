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

# Codando #
lista = [6,7,8,3,10,19,4,1,0,61,30,16,17,82,29,34,43,21,11,39,56,67,12]
def bubble_sort(arr):
    n = len(arr)
    # Para cada elemento i do array
    for i in range(n):
        #Para cada elemento j do array
        for j in range(0, n-i-1):
            #Se elemento i for maior que elemento j
            if arr[j] > arr[j+1]:
                #Troque os elementos i e j
                arr[j], arr [j+1] = arr[j+1], arr[j]
    return  arr 