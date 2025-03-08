import threading as th
import time

cont = 0 #Recurso compartilhado
L = th.Lock() #Bloqueio para evitar errros aos diferentes threads acessarem uma mesma variável.

def incrementar():
    L.acquire()
    try:
        global cont
        for _ in range(1000):
            cont =  cont + 1
    finally:
        L.release() #Liberar o uso da variável.
    
Ta = th.Thread(target= incrementar)
Tb = th.Thread(target= incrementar)
Tc = th.Thread(target= incrementar)

Ta.start()
Tb.start()
Tc.start()

Ta.join()
Tb.join()
Tc.join()

print(f"Contador: {cont}")
