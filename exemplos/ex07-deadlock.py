import threading as th
import time

cont = 0 #Recurso compartilhado
L1 = th.Lock()
L2 = th.Lock()

def tarefa1():
    print("Tentando adquirir o Lock1")
    L1.acquire()
    time.sleep(1)
    L2.acquire()
    print("Tentando adquirir o Lock2")
    L2.release()
    L1.release()
    
def tarefa2():
    print("Tentando adquirir o Lock2")
    L2.acquire()
    time.sleep(1)
    L1.acquire()
    print("Tentando adquirir o Lock1")
    L2.release()
    L1.release()

t1 = th.Thread(target= tarefa1)
t2 = th.Thread(target= tarefa2)
t1.start()
t2.start()
t1.join()
t2.join()

print("Programa encerrado!")