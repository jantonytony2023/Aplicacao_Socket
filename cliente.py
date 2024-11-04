import socket

def cliente_tcp(mensagem):
    # Criando um socket TCP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Conectando ao servidor na porta 5000
    cliente_socket.connect(('localhost', 5000))
    
    # Enviando a mensagem
    cliente_socket.sendall(mensagem.encode('utf-8'))
    
    # Recebendo a resposta do servidor
    resposta = cliente_socket.recv(1024).decode('utf-8')
    print(f"Resposta do servidor: {resposta}")
    
    # Fechando a conexão
    cliente_socket.close()

def cliente_udp(mensagem):
    # Criando um socket UDP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Enviando a mensagem para o servidor na porta 5001
    cliente_socket.sendto(mensagem.encode('utf-8'), ('localhost', 5001))
    
    # Recebendo a resposta do servidor
    resposta, _ = cliente_socket.recvfrom(1024)
    print(f"Resposta do servidor: {resposta.decode('utf-8')}")
    
    # Fechando o socket
    cliente_socket.close()

def main():
    # Solicitando ao usuário o protocolo e a mensagem
    protocolo = input("Escolha o protocolo (TCP/UDP): ").strip().upper()
    mensagem = input("Digite a mensagem a ser enviada: ")
    
    if protocolo == 'TCP':
        cliente_tcp(mensagem)
    elif protocolo == 'UDP':
        cliente_udp(mensagem)
    else:
        print("Protocolo inválido. Por favor, escolha TCP ou UDP.")

if __name__ == "__main__":
    main()


