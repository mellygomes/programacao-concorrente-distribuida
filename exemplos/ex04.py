import threading as th
import time

def saudacao(nome, tempo):
    print(f"Olá, {nome}!")
    time.sleep(tempo)
    print(f"Tchau, {nome}.")
  
Ta = th.Thread(target=saudacao, args=("Marcelo", 4))    
Tb = th.Thread(target=saudacao, args=("Ana", 2))    

t0 = time.time()

Ta.start()
Tb.start()
Ta.join()
Tb.join()

tf = time.time()
deltat = tf - t0

print(f"Tempo de processamento: {round(deltat, 3)}\n")
print("Thread principal finalizada.\n")