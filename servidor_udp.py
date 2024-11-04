import socket

def servidor_udp():
    # Criando um socket UDP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind do socket a porta 5001
    servidor_socket.bind(('0.0.0.0', 5001))
    print("Servidor UDP escutando na porta 5001...")
    
    while True:
        # Recebendo dados do cliente
        dados, endereco = servidor_socket.recvfrom(1024)
        dados_decodificados = dados.decode('utf-8')
        print(f"Recebido de {endereco}: {dados_decodificados}")
        
        # Enviando resposta
        resposta = f"UDP: {dados_decodificados}"
        servidor_socket.sendto(resposta.encode('utf-8'), endereco)

if _name_ == "_main_":
    servidor_udp()