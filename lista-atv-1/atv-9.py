# Crie um programa que liste todos os processos ativos no sistema, ordenados pelo uso de memória
# física (RSS), em ordem decrescente. Exiba o PID, nome e uso de memória (em MB) de cada processo.
# Dica:
# Itere sobre psutil.process_iter() para recuperar memory_info().rss de cada processo, ordene os
# processos pelo valor de RSS e exiba os resultados.

# Desenvolva um script que identifique o processo que está consumindo mais CPU no momento.
# Dica:
# Use psutil.process_iter() para iterar sobre os processos e recupere o atributo cpu_percent() de cada
# processo. Ordene os resultados e exiba o PID e o nome do processo com maior uso de CPU.

import psutil as ps

print("\nLista ordenada de processos consumindo maior quantidade em MB de memória física (RSS): \n")

processos = []

for proc in ps.process_iter():
    try:
        info = proc.as_dict(attrs=['name', 'pid'])
        info['rss'] = (proc.memory_info().rss / (1024 * 1024))
        processos.append(info)
    except (ps.NoSuchProcess, ps.AccessDenied):
        pass

sorted_list = sorted(processos, key=lambda x: x['rss'], reverse=True)

for a in sorted_list:
    print(f"Processo: {a['name']} (PID: {a['pid']}) - Uso de RSS: {round(a['rss'], 2)} MB.")

print("\n")