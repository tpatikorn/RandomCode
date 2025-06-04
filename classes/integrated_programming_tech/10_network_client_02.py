import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5000
s.connect((host, port))
msg = 'Hello server'


def communicate(data):
    s.send(data.encode(encoding='UTF-8', errors='strict'))
    data = s.recv(1024)
    result = data.decode(encoding='UTF-8', errors='strict')
    print(data.decode(encoding='UTF-8', errors='strict'))
    return


while True:
    msg = input("What's your message: ")
    communicate(msg)
