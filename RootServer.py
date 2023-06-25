from socket import *

# 定义一个二维字符串数组，用于存储域名扩展名和对应的端口号
records = [
    ["com", 60001, "A"],
    ["edu", 60002, "A"],
    ["cn", 60003, "A"]
]

serverPort = 55555
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The root server is ready")
while True:
    request, clientAddress = serverSocket.recvfrom(2048)
    target = request.decode().rsplit(".", 1)[-1]
    result = ""
    for record in records:
        if record[0] == target:
            result = record[1]
            break
    serverSocket.sendto(str(result).encode(), clientAddress)
