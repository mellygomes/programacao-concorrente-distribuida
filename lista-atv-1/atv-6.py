# Crie um script que liste todos os processos que estão em estado "sleeping".
# Dica:
# Filtre os processos usando proc.info['status'] == psutil.STATUS_SLEEPING.

import psutil as ps

print('Lista de processos em estado SLEEPING\n')

for proc in ps.process_iter():
    info = proc.as_dict(attrs=['name', 'pid', 'status'])
    if (info['status'] == ps.STATUS_SLEEPING):
        print('Processo: {} (PID: {}) - {}'.format(info['name'], info['pid'], info['status'] ))
    else:
        continue

print("\n")