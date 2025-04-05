from time import time
import random
import threading

def SomaQuadrados(Dados, Media):
    Soma = 0

    for x in Dados: Soma = Soma + (x - media) **2
    return Soma

def calcularVariancia(Dados):
    N = len(Dados)
    # Soma = 0
    # for x in Dados: Soma = Soma + x
    # Media = Soma / N

    # SomaDQ = 0
    # for x in Dados: SomaDQ = SomaDQ + (x - Media) **2
    # Variancia = SomaDQ / N

    Meio = N // 2
    Esquerda = Dados[:Meio] 
    Direito = Dados[Meio:]

    SQesquerda = 0 
    SQdireita = 0 

    def ProcessarEsquerda():
        nonlocal SQesquerda
        SQesquerda = SomarQuadrados(Esquerda, Media)
    def ProcessarDireita():
        nonlocal SQdireita
        SQdireita = SomarQuadrados(Direita, Media)

    TE = threading.Thread(target = ProcessarEsquerda)
    TD = threading.Thread(target = ProcessarDireita)

    TE.start()
    TE.Join()
    TD.start()
    TD.Join()

    SQTotal = SQDireita + SQEsquerda
    Variancia = SQTotal / N
    return Variancia

L1 = [2, 4, 6, 8, 10]
L2 = [2, 2, 2, 2, 2]
L3 = [random.randint(1, 100) for _ in range(100)]

t0 = time()
teste1 = calcularVariancia(L3)
t1 = time()
print(f"\nTeste 1: {teste1}\tTempo de execução: {t0 - t1:.6f}\n")

# SpeedUp = aceleração do código