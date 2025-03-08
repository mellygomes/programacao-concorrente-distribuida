import threading as th
import time

cont = 0 #Recurso compartilhado

def incrementar():
    global cont
    for _ in range(1000):
        x = cont
        time.sleep(0.0001)
        x = x + 1
        cont =  x
    
listaDeThreads = []

for _ in range(50):
    T = th.Thread(target= incrementar)
    listaDeThreads.append(T)
    T.start()

for t in listaDeThreads:
    t.join()

print(f"Valor final do contador: {cont}")
