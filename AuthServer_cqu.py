from socket import *

# 定义一个二维字符串数组，用于存储域名扩展名和对应的端口号
records = [
    ["my.cqu.edu", "114.514.34.1", "A"],
    ["i.cqu.edu", "114.514.34.2", "A"],
    ["jwc.cqu.edu", "114.514.34.3", "A"],
    ["mail.cqu.edu", "114.514.34.4", "A"],
    ["huxi.cqu.edu", "114.514.34.5", "A"],
    ["ugs.cqu.edu", "114.514.34.6", "A"]
]

serverPort = 60032
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The authoritative server of CQU is ready")
while True:
    request, clientAddress = serverSocket.recvfrom(2048)
    result = ""
    for record in records:
        if record[0] == request.decode():
            result = record[1]
            break
    serverSocket.sendto(result.encode(), clientAddress)
