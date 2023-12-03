import socket

# Class modeled lightly after https://docs.python.org/3.4/howto/sockets.html
# This is used by both the client and the server and handles sending messages back and forth
class GameSocket:

    def __init__(self, sock):
        self.sock = sock

    # Sets up as a server for listening
    def initServer(self):
        self.sock.bind(('localhost', 12525))
        self.sock.listen(1)
        (clientsocket, clientaddress) = self.sock.accept()
        self.sock = clientsocket
        self.clientaddress = clientaddress

    # Sets up as a client and connects to a server
    def initClient(self):
        self.sock.connect(('localhost', 12525))

    # Sends a message efficiently using dynamic message lengths
    def send(self, msg):
        msgLen = bytes(f"{len(msg)}".zfill(4), 'utf-8')
        self.sock.send(msgLen)

        sent = self.sock.send(bytes(msg, 'utf-8'))
        if sent == 0:
            raise RuntimeError("socket connection broken")

    # Recieves a message utilizing the msg length
    def receive(self):
        msgLen = self.sock.recv(4)
        if msgLen == b'':
            raise RuntimeError("socket connection broken")
        msgLen = int(msgLen)
        
        return str(self.sock.recv(msgLen), 'utf-8')
    
    # Closes the socket
    def close(self):
        self.sock.close()