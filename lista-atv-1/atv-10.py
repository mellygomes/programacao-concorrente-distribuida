# Desenvolva um script que identifique e liste todos os processos que estão consumindo mais de 50% da
# CPU no momento. Exiba o PID, nome e uso de CPU de cada processo.
# Dica:
# Use psutil.process_iter() para iterar sobre os processos e recupere cpu_percent() de cada processo.
# Filtre os processos onde cpu_percent() é maior que 50 e exiba os resultados.
import psutil as ps

print("\nProcessos utilizando mais de 50% da CPU: \n")

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
        if (info['cpu'] > 50.0):
            processos.append(info)
    except (ps.NoSuchProcess, ps.AccessDenied):
        pass


for a in processos:
    print(f"Processo: {a['name']} (PID: {a['pid']}) - CPU: {a['cpu']}%")

print("\n")
