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

        # Check if the user is quitting out of the application
        if input == '/q':
            sock.close()
            break
        
        # If there is a game, we run the input through that
        if game != None:
            # Run the users command
            (gameOver, msg) = game.choice(input)
            # Exit if it was a word guess
            if gameOver:
                game = None
                sock.send(msg)
                continue
            # Check if the user won
            (won, msg) = game.getOutput()
            if won:
                game = None
            sock.send(msg)
            continue

        # If there is no game started and the game command was issued, start one
        if input == 'game':
            game = Game() # Initialize a new game
            sock.send(game.getEntryMessage())
            continue

        sock.send('Command Not Found!')

mainLoop()