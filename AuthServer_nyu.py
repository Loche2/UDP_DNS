from socket import *

# 定义一个二维字符串数组，用于存储域名扩展名和对应的端口号
record = [
    ["root", 55555, "A"]
]


def send(server_name, server_port, domain):
    client_socket = socket(AF_INET, SOCK_DGRAM)
    client_socket.sendto(domain.encode(), (server_name, server_port))
    result, server_address = client_socket.recvfrom(2048)
    print("answer: "+result.decode())
    client_socket.close()
    return result.decode()


serverPort = 60010
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The authoritative server of NYU is ready")
while True:
    request, clientAddress = serverSocket.recvfrom(2048)
    print("askRoot")
    resultFromRoot = send('localhost', record[0][1], request.decode())
    print("recvRoot")
    if not resultFromRoot:
        serverSocket.sendto("404".encode(), clientAddress)
        print("404 not found\n")
        continue
    print("askTLD")
    resultFromTLD = send('localhost', int(resultFromRoot), request.decode())
    print("recvTLD")
    if not resultFromTLD:
        serverSocket.sendto("404".encode(), clientAddress)
        print("404 not found\n")
        continue
    print("askAuth")
    resultFromAuth = send('localhost', int(resultFromTLD), request.decode())
    print("recvAuth")
    if not resultFromAuth:
        serverSocket.sendto("404".encode(), clientAddress)
        print("404 not found\n")
        continue
    serverSocket.sendto(resultFromAuth.encode(), clientAddress)
    print("sendClient\n")
