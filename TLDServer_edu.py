from socket import *

# 定义一个二维字符串数组，用于存储域名扩展名和对应的端口号
records = [
    ["nyu.edu", "dns.nyu.edu", "NS"],
    ["dns.nyu.edu", 60012, "A"],
    ["umass.edu", "dns.umass.edu", "NS"],
    ["dns.umass.edu", 60022, "A"],
    ["cqu.edu", "dns.cqu.edu", "NS"],
    ["dns.cqu.edu", 60032, "A"]

]

serverPort = 60002
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The TLD server of .edu is ready")
while True:
    request, clientAddress = serverSocket.recvfrom(2048)
    target = request.decode().rsplit(".", 2)
    target = target[-2]+'.'+target[-1]
    print(target)
    result = ""
    for record in records:
        if record[0] == target:
            target = record[1]
            break
    for record in records:
        if record[0] == target:
            result = record[1]
            break
    serverSocket.sendto(str(result).encode(), clientAddress)
