import time
import threading

def tarefa(id):
    print(f"Tarefa {id} iniciada")
    time.sleep(2)
    print(f"Tarefa {id} concluída")

def main_sequencial():
    t0 = time.time()
    for i in range(4): tarefa(i)
    t1 = time.time()

    return t1 - t0

def main_paralela():
    t0 = time.time()
    threads = []
    	
    for i in range(4):
        threads = threading.Thread(target = tarefa, args = (i,))
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()
    t1 = time.time()

    return t1 - t0

# Versão sequencial

t_seq = main_sequencial()
t_par = main_paralela()
print(f"Sequencial: {t_seq}")
print(f"Paralela: {t_par}")

speedUp = t_par - t_seq