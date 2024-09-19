import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9090))


def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            print('An error occurred!')
            client.close()
            break


def send():
    while True:
        message = input()
        client.send(message.encode())
        if message == 'exit':
            break


receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
