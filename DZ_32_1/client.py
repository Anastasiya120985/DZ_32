import socket


def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9090))

    response = client_socket.recv(1024).decode()
    print(response)
    if response.lower() == "You initiated the game. Do you want to play Tic Tac Toe? (yes/no)":
        answer = input("Do you want to play Tic Tac Toe? (yes/no): ")
        client_socket.send(answer.encode())

        response = client_socket.recv(1024).decode()
        print(response)

    client_socket.close()


if __name__ == "__main__":
    connect_to_server()