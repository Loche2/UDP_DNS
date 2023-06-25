from socket import *

serverName = 'localhost'
serverPort = 60010
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    domain = input('Input domain to resolve:')
    clientSocket.sendto(domain.encode(), (serverName, serverPort))
    address, serverAddress = clientSocket.recvfrom(2048)
    if address.decode() == "404":
        print("404 not found, please retry\n")
        continue
    print("The \"IP address\" of " + domain + " is " + address.decode() + "\n")
# clientSocket.close()
