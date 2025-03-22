import threading as th
import time

def tarefa():
    print("\nInicio...")
    time.sleep(3)
    print("Fim.\n")
    
T = th.Thread(target=tarefa)
T.start() #inicia a thread
T.join() #Sem o join, o codigo continua executando mesmo enquanto a thread ainda não está encerrada
print("Thread principal finalizada.\n")