import socket

def iniciar_cliente():
    # Configuração do cliente
    HOST = '127.0.0.1' # Endereço do servidor
    PORT = 65432 # Porta do servidor
    # Criando o socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT)) # Conecta ao servidor
        print("Conectado ao servidor. Solicitando data e hora...")
        # Envia a solicitação ao servidor
        s.sendall(b"data e hora")
        # Envia a solicitação ao servidor
        s.sendall(b"data e hora")
        # Recebe a resposta do servidor
        data = s.recv(1024)
        # Exibe a resposta
        print(f"Resposta do servidor: {data.decode()}")
        
if __name__ == "__main__":
    iniciar_cliente()