import random
import time
import threading as th

# Função principal do QuickSort (Deixamos a função original aqui para podermos fazer as comparações de tempo, mas ela não será chamada)
def quicksort(arr):
    time.sleep(0.01) # Adicionamos um atraso artificial para conseguirmos medir a diferença nos tempos de execução

    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]  # Elementos menores ou iguais ao pivô
    right = [x for x in arr[:-1] if x > pivot]  # Elementos maiores que o pivô

    return quicksort(left) + [pivot] + quicksort(right)

# Função QuickSort com a implementação de threads
def quicksort_paralelizada(arr):
    time.sleep(0.01) # Atraso para medir o tempo

    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]  # Elementos menores ou iguais ao pivô
    right = [x for x in arr[:-1] if x > pivot]  # Elementos maiores que o pivô

    leftList = []
    rightList = []

    threadLeft = th.Thread(target=lambda: leftList.extend(quicksort_paralelizada(left)))
    threadRight = th.Thread(target=lambda: rightList.extend(quicksort_paralelizada(right)))

    threadLeft.start()
    threadRight.start()
    threadLeft.join()
    threadRight.join()

    return leftList + [pivot] + rightList

# Função para gerar números aleatórios
def gerar_numeros_aleatorios(n=500, min_val=1, max_val=200):
    return [random.randint(min_val, max_val) for _ in range(n)]

# Função principal para testar o QuickSort
if __name__ == "__main__":
    numeros = gerar_numeros_aleatorios() 
    print(f"\nPrimeiros 10 números antes da ordenação: {numeros[:10]}\n") 
    # Adicionamos '[:10]' para de fato mostrar apenas os 10 primeiros numeros e facilitar a visualização no terminal 

    inicio = time.time()
    numeros_ordenados = quicksort_paralelizada(numeros)
    fim = time.time()
    tempoExecucao = fim - inicio
   
    print(f"Primeiros 10 números após a ordenação: {numeros_ordenados[:10]}\n")
    print(f"Tempo de execução: {tempoExecucao:.5f}\n")    