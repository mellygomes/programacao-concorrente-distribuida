# Desenvolva um programa que calcule a soma da memória física (RSS) usada por todos os processos
# ativos no sistema.
# Dica:
# Itere sobre psutil.process_iter(), recupere memory_info().rss de cada processo e some os valores.
import psutil as ps

soma = 0

for proc in ps.process_iter():
    try:
        soma += (proc.memory_info().rss / (1024 * 1024))
    except (ps.NoSuchProcess, ps.AccessDenied):
        pass

print(f"\nSoma da memória total utilizada: {round(soma, 2)} MB.\n")