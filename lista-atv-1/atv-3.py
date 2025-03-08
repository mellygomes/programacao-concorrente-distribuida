# Escreva um programa que monitore continuamente o uso de memória física (RSS) de um processo
# específico, dado seu PID.
# Dica:
# Use um loop para chamar process.memory_info().rss periodicamente e exibir o valor em MB.
import psutil as ps

print('\n Monitoramento de...: \n')

def obter_memoria_processo(pid):
    try:
        # Obter informações do processo
        processo = ps.Process(pid)
        memoria_info = processo.memory_info()
        # Converter para MB
        memoria_fisica_mb = memoria_info.rss / (1024 * 1024) # Resident Set Size
        memoria_virtual_mb = memoria_info.vms / (1024 * 1024) # Virtual Memory Size
        return memoria_fisica_mb, memoria_virtual_mb
    except ps.NoSuchProcess:
        return None, None

pid = 0

memoria_fisica, memoria_virtual = obter_memoria_processo(pid)
if memoria_fisica is not None:
    print(f"Processo PID {pid}:")
    print(f"Memória Física (RSS): {memoria_fisica:.2f} MB")