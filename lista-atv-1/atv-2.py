# Desenvolva um script que identifique o processo que está consumindo mais CPU no momento.
# Dica:
# Use psutil.process_iter() para iterar sobre os processos e recupere o atributo cpu_percent() de cada
# processo. Ordene os resultados e exiba o PID e o nome do processo com maior uso de CPU.

import psutil as ps

print('\nLista de processos ordenados consumindo mais CPU: \n')

processos = []

# primeiro loop para inicializar a medição de cpu
for proc in ps.process_iter():
    try:
        proc.cpu_percent(interval=None)  # inicializa a coleta de dados
    except (ps.NoSuchProcess, ps.AccessDenied):
        pass  #ignora processos inacessíveis

# aguarda um tempo para medir corretamente
ps.cpu_percent(interval=0.5)

for proc in ps.process_iter():
    try:
        info = proc.as_dict(attrs=['name', 'pid'])
        info['cpu'] = proc.cpu_percent(interval=None)
        processos.append(info)
    except (ps.NoSuchProcess, ps.AccessDenied):
        pass

sorted_list = sorted(processos, key=lambda x: x['cpu'], reverse=True)

for a in sorted_list:
    print(f"Processo: {a['name']} (PID: {a['pid']}) - CPU: {a['cpu']}%")

print("\n")