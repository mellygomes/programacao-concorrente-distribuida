import threading as th

# Uso de semáfaro em threads
S = th.Semaphore(3)

def trabalho(ID):
    print(f"Thread {ID} iniciou.")
    
    with S:
        print(f"Thread {ID} passou pelo semáforo")
        th.Event().wait(1)
        print(f"Thread {ID} liberou o recurso.")

threads = [th.Thread(target = trabalho, args=(i,)) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()