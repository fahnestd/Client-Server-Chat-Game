import socket
from gameSocket import GameSocket
from game import Game

sock = GameSocket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

sock.initServer() # Sets this as the server program

print(f"Client {sock.clientaddress} joined the chat!")


def handleInput(input, game):
    # Check if the user is quitting out of the application
    if input == '/q':
        sock.close()
        exit()
    
    # If there is a game, we run the input through that
    if game != None:
        # Run the users command
        (gameOver, msg) = game.choice(input)
        # Exit if it was a word guess
        if gameOver:
            game = None
            return game, msg
            
        # Check if the user won
        (won, msg) = game.getOutput()
        if won:
            game = None
        return game, msg

    # If there is no game started and the game command was issued, start one
    if input == 'game':
        game = Game() # Initialize a new game
        return game, game.getEntryMessage()
    
    # Otherwise, there is no msg to return
    return game, ''

# Gets the users input from the CLI
def getInput():
    userInput = ''
    # Recursivly get input until user enters something
    while userInput == '':
        userInput = input("Enter Input > ")
    return userInput
        

def mainLoop():
    game = None
    while True:
        # Client Goes First
        input = sock.receive()
        game, msg = handleInput(input, game)
        print('Client: ' + input)
        print(msg)

        # Then the server goes
        input = getInput()
        game, input2 = handleInput(input, game)
        print(input2)

        sock.send(msg + '\nServer: ' + input + '\n' +  input2)

mainLoop()