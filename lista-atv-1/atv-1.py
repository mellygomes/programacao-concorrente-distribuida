# Crie um programa que liste todos os processos ativos no sistema, exibindo seus PIDs, nomes e estados
# (ex.: "running", "sleeping").
# Dica:
# Itere sobre psutil.process_iter() e recupere os atributos pid, name e status.


import psutil as ps

print('Lista de processos em execução\n')

for proc in ps.process_iter():    
    info = proc.as_dict(attrs=['name', 'pid', 'status'])
    print('Processo: {} (PID: {}) - {}'.format(info['name'], info['pid'], info['status'] ))