import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9090))
server.listen()

clients = []


def broadcast(message, client):
    for c in clients:
        if c != client:
            c.send(message)


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            clients.remove(client)
            client.close()
            break


while True:
    client, addr = server.accept()
    clients.append(client)
    print(f'Connection from {addr} established.')
    client.send('Welcome to the chat!'.encode())
    client.send('Please enter your username:'.encode())
    username = client.recv(1024).decode()
    client.send('Please enter your password:'.encode())
    password = client.recv(1024).decode()
    client.send('You are now connected to the chat!'.encode())
    broadcast(f'{username} has joined the chat!'.encode(), client)
    client.send('Start chatting!'.encode())
    client.send("Type 'exit' to leave the chat.".encode())

    handle_client(client)