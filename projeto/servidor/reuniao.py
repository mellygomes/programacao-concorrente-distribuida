import socket
from datetime import datetime

class Reuniao:
    def __init__(self, HOST, PORT) -> None:
        self.HOST = HOST
        self.PORT = PORT

    def iniciar_servidor(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            self.server = server
            self.server.bind((self.HOST, self.PORT)) # Associa o socket ao endereço e porta
            self.server.listen() # Habilita o servidor para aceitar conexões
            print(f"Servidor ouvindo em {self.HOST} : {self.PORT}")
                    
        while True:
            conn, addr = self.server.accept()
            with conn:
                print(f"Conectado por {addr}")
                while True:
                    # Recebe dados do cliente
                    data = conn.recv(1024)
                    if not data:
                        break
                    # Verifica se o cliente pediu a data e hora
                    if data.decode().strip().lower() == "data e hora":
                        # Obtém a data e hora atuais
                        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        resposta = f"Data e hora atual: {agora}"
                        conn.sendall(resposta.encode()) # Envia a resposta ao cliente
                    else:
                        conn.sendall(b"Mensagem invalida")


R = Reuniao('127.0.0.1', 65432)
R.iniciar_servidor()