# Desenvolva um programa que monitore o uso de disco (leitura/escrita) de um processo específico,
# dado seu PID.
# Dica:
# Use psutil.Process(pid).io_counters() para recuperar as estatísticas de leitura/escrita de disco.

import psutil as ps 

def encerrar_processo(pid):
    try:
        processo = ps.Process(pid)
    except ps.NoSuchProcess:
        print(f"Processo com PID {pid} não encontrado.")
    except ps.AccessDenied:
        print(f"Acesso negado ao processo com PID {pid}.")
    except ps.TimeoutExpired:
        print(f"O processo com PID {pid} não pôde ser encerrado dentro do tempo limite.")