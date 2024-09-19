import socket


def start_game():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9090))
    server_socket.listen(2)
    print("Waiting for players to connect...")

    player1, addr1 = server_socket.accept()
    print("Player 1 connected from", addr1)
    player1.send("You initiated the game. Do you want to play Tic Tac Toe? (yes/no)".encode())
    response = player1.recv(1024).decode()

    if response.lower() == "yes":
        player2, addr2 = server_socket.accept()
        print("Player 2 connected from", addr2)
        player2.send("Player 1 initiated the game. Do you want to play Tic Tac Toe? (yes/no)".encode())
        response = player2.recv(1024).decode()

        if response.lower() == "yes":
            player1.send("Game started! Let's play Tic Tac Toe.")
            player2.send("Game started! Let's play Tic Tac Toe.")
            # logic game Tic Tac Toe
        else:
            player1.send("Player 2 does not want to play. Game over.")
            player2.send("You declined to play. Game over.")
    else:
        player1.send("You declined to play. Game over.")

    player1.close()
    player2.close()
    server_socket.close()


if __name__ == "__main__":
    start_game()