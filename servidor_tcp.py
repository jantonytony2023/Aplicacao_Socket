import socket

def servidor_tcp():
    # Criando um socket TCP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind do socket a porta 5000
    servidor_socket.bind(('0.0.0.0', 5000))
    
    # Colocando o socket em modo de escuta
    servidor_socket.listen(5)
    print("Servidor TCP escutando na porta 5000...")
    
    while True:
        # Aceitando uma conexão
        cliente_socket, endereco = servidor_socket.accept()
        print(f"Conexão recebida de {endereco}")
        
        # Recebendo dados do cliente
        dados = cliente_socket.recv(1024).decode('utf-8')
        print(f"Recebido: {dados}")
        
        # Enviando resposta
        resposta = f"TCP: {dados}"
        cliente_socket.sendall(resposta.encode('utf-8'))
        
        # Fechando a conexão
        cliente_socket.close()

if __name__ == "__main__":
    servidor_tcp()
