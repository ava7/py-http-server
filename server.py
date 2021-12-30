
from socket import *

serverPort = 1337
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # https://stackoverflow.com/a/337137
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("Server is ready to receive...")

try:
    while True:
        connectionSocket, address = serverSocket.accept()
        print('Connection established. Client connected: ', address)

        sentence = connectionSocket.recv(1024).decode()
        connectionSocket.send(sentence.upper().encode())
        connectionSocket.close()
except KeyboardInterrupt:
    print('Killed by user.')
