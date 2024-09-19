import socket

client = socket.socket()
client.connect((socket.gethostname(), 9090))

file = open('test.txt', 'wb')
print('Получение данных с сервера')
while True:
    data = client.recv(1024)
    file.write(data)
    if not data:
        break
file.close()
print('Данные сохранены')
client.close()