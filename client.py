import socket
from gameSocket import GameSocket

sock = GameSocket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

sock.initClient() # Sets this as the client program

print("Successfully connected to server!")
print("Enter command 'game' to start a game!")

def mainLoop():
    
    while True:
        userInput = ''
        while userInput == '':
            userInput = input("Enter Input > ")
        sock.send(userInput)
        if userInput == '/q':
            sock.close()
            break

        response = sock.receive()
        # Handle the servers response
        print(f"{response}")
        pass
    
mainLoop()