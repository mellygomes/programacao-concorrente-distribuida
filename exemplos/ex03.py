import threading as th
import time

def tarefa():
    print("\nInicio...")
    time.sleep(2)
    print("Fim.\n")
    
Ta = th.Thread(target=tarefa)
Tb = th.Thread(target=tarefa)

t0 = time.time()

Ta.start() 
Tb.start()
Ta.join()
Tb.join()

tf = time.time()
deltat = tf - t0

print(f"Tempo gasto {deltat}") #Sendo executadas de forma paralela, as duas gastam +/- a metade do tempo que levariam sendo executadas em série.
print("Thread principal finalizada.\n")