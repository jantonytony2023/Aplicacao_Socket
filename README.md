# Servidor e Cliente em Python

Este projeto implementa um servidor UDP e um servidor TCP simples em Python, além de um cliente que pode se comunicar com ambos. 

## Funcionalidades

- **Servidor UDP:**
  - Escuta na porta 5001.
  - Recebe mensagens de clientes e responde com o prefixo "UDP:".

- **Servidor TCP:**
  - Escuta na porta 5000.
  - Aceita conexões de clientes e responde com o prefixo "TCP:".
  

- **Cliente:**
  - Envia mensagens para o servidor UDP e TCP.
  - Recebe e exibe as respostas dos servidores.

## Como Executar

### Para o Servidor

1. Certifique-se de ter o Python instalado em seu sistema.
2. Salve o código do servidor UDP em um arquivo chamado `servidor_udp.py`.
3. Salve o código do servidor TCP em um arquivo chamado `servidor_tcp.py`.
4. Execute o servidor UDP e o servidor TCP:

   ```bash
   python servidor_udp.py
   python servidor_tcp.py

### Para o Cliente
  
  python cliente.py
