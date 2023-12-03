import socket
from gameSocket import GameSocket

sock = GameSocket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

sock.initClient() # Sets this as the client program

print("Successfully connected to server!")
print("Enter command 'game' to start a game!")

def mainLoop():
    while True:
        userInput = ''
        # Recursivly get input until user enters something
        while userInput == '':
            userInput = input("Enter Input > ")
        sock.send(userInput)

        # Handle the user issuing the quit command
        if userInput == '/q':
            sock.close()
            break

        response = sock.receive()
        # Handle the servers response
        print(f"{response}")
        pass
    
mainLoop()