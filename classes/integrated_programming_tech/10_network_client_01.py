import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '172.20.254.131'
port = 5001
try:
    s.connect((host, port))
    msg = 'นักศึกษามาสายยยยยยยยยย'
    s.send(msg.encode(encoding='UTF-8', errors='strict'))
    data = s.recv(1024)
    print(data.decode(encoding='UTF-8', errors='strict'))
    s.close()
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
