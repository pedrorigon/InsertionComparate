import time
import math
import random


def insertion_sort(array):
    trocas = comparacoes = 0
    # do segundo ao último (o primeiro faz parte do subarray ordenado)
    for i in range(1, len(array)):
        # chave a inserir no subarray ordenado
        chave = array[i]
        j = i-1                                # último elemento do subarray ordenado
        # busca linear da direita para a esquerda no subarray ordenado
        while (j >= 0) and (array[j] > chave):
            comparacoes = comparacoes + 1
            array[j+1] = array[j]
            j = j - 1
            trocas = trocas + 1
        array[j+1] = chave
        trocas = trocas + 1
    # retorna quantidade de operações
    #return {'trocas': trocas, 'comparacoes': comparacoes}


def shell_sort(array):
    trocas = comparacoes = 0
    # Dividindo o vetor em h segmentos
    h = len(array) // 2
    while h > 0:
        i = h
        while i < len(array):
            chave = array[i]  # chave a inserir no subarray ordenado
            troca_flag = False
            j = i-h                                # último elemento do subarray ordenado
            while (j >= 0) and (array[j] > chave):
                comparacoes = comparacoes + 1
                array[j+h] = array[j]
                troca_flag = True
                j = j - h
                trocas = trocas + 1
                if troca_flag:
                    array[j+h] = chave
                    trocas = trocas + 1
            i = i + 1
        h = h // 2    
    # retorna quantidade de operações
    #return {'trocas': trocas, 'comparacoes': comparacoes}


vetor = list(range(0, 10000))
random.shuffle(vetor)
antes = time.time()
#shell_sort(vetor)
insertion_sort(vetor)
depois = time.time()
total = (depois-antes)*1000

print(vetor)

print(f'o tempo total foi de {total:.2f} ms')
