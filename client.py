from socket import *

serverName = 'localhost'
serverPort = 1337

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input("Input message: ")
clientSocket.send(sentence.encode())

response = clientSocket.recv(1024)
print('From server: ', response.decode())

clientSocket.close()
