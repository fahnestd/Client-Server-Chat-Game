import socket
from gameSocket import GameSocket
from game import Game

sock = GameSocket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

sock.initServer() # Sets this as the server program

print(f"Client {sock.clientaddress} joined the chat!")


def mainLoop():
    game = None
    while True:
        input = sock.receive()
        if input == '/q':
            sock.close()
            break
        
        if game != None:
            (gameOver, msg) = game.choice(input)
            if gameOver:
                game = None
                sock.send(msg)
                continue
            (won, msg) = game.getOutput()
            if won:
                game = None
            sock.send(msg)
            continue

        if input == 'game':
            game = Game() # Initialize a new game
            sock.send(game.getEntryMessage())
            continue

        sock.send('Command Not Found!')

mainLoop()