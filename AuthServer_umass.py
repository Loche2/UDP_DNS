from socket import *

# 定义一个二维字符串数组，用于存储域名扩展名和对应的端口号
records = [
    ["gaia.cs.umass.edu", "114.514.00.1", "A"],
    ["cs.umass.edu", "114.514.00.2", "A"],
    ["mail.umass.edu", "114.514.00.3", "A"]
]

serverPort = 60022
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The authoritative server of UMASS is ready")
while True:
    request, clientAddress = serverSocket.recvfrom(2048)
    result = ""
    for record in records:
        if record[0] == request.decode():
            result = record[1]
            break
    serverSocket.sendto(result.encode(), clientAddress)
