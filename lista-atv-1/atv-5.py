# Crie um script que liste todos os processos que estão usando mais de 100 MB de memória física (RSS).
# Dica:
# Filtre os processos onde memory_info().rss / (1024 * 1024) é maior que 100.

import psutil as ps

print("\nProcessos utilizando mais de 100MB de memória física (RSS): \n") 

for proc in ps.process_iter():
    try:
        info = proc.as_dict(attrs=['name', 'pid'])
        info['rss'] = proc.memory_info().rss / (1024 * 1024)
        if ((info['rss'] > 100)):
            print(f"{info['name']} (PID: {info['pid']}) - Utilizando: {round(info['rss'], 2)} MB.")
    except (ps.NoSuchProcess, ps.AccessDenied):
        pass

print("\n")