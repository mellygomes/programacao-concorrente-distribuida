# Escreva um programa que monitore o uso de rede (bytes enviados e recebidos) de um processo
# específico, dado seu PID. Exiba os valores periodicamente.
# Dica:
# Use psutil.Process(pid).io_counters() ou psutil.net_io_counters() para recuperar as estatísticas de rede
# do processo. Atualize os valores em intervalos regulares usando um loop.
