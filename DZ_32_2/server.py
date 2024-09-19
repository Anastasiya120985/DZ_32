import socket

server = socket.socket()
server.bind(('localhost', 9090))
server.listen(5)

print('Сервер запущен')

con, _ = server.accept()
file = open('hello.txt', 'rb')
print('Отправка данных клиенту')
line = file.read(1024)
while line:
    con.send(line)
    line = file.read(1024)

file.close()
con.close()
server.close()
