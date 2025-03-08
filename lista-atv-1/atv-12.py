# Crie um script que liste todos os processos que estão usando mais de 1 GB de memória virtual (VMS).
# Exiba o PID, nome e uso de memória virtual (em GB) de cada processo.
# Dica:
# Filtre os processos onde memory_info().vms / (1024 * 1024 * 1024) é maior que 1 e exiba os
# resultados.

import psutil as ps

print("\nProcessos utilizando mais de 0.5GB de memória virtual (VMS): \n") #só coloquei 0.5 porque é muito difícil ter um com mais de 1GB ^-^

for proc in ps.process_iter():
    try:
        info = proc.as_dict(attrs=['name', 'pid'])
        info['vms'] = proc.memory_info().vms / (1024 * 1024 * 1024)
        if ((info['vms'] > 0.5)):
            print(f"{info['name']} (PID: {info['pid']}) - Utilizando: {round(info['vms'], 1)} GB de VMS.")
    except (ps.NoSuchProcess, ps.AccessDenied):
        pass

print("\n")