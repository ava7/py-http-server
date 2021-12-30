
from socket import *
from pathlib import Path

serverPort = 1337
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # https://stackoverflow.com/a/337137
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("Server is ready to receive...")

try:
    while True:
        connectionSocket, address = serverSocket.accept()
        print("Connection established. Client connected: ", address)

        request = connectionSocket.recv(1024).decode()

        url = request.split()[1]
        print("Requested resource: ", url)
        location = Path("./www" + url)
        if url == '/':
            location = Path("./www/index.html")

        try:
            data = Path(location).read_text()
        except FileNotFoundError:
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
            connectionSocket.close()
            continue

        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(data.encode())
        connectionSocket.close()
except KeyboardInterrupt:
    print('Killed by user.')
