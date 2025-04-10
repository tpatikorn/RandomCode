import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("starting")
server = 'booklove-anime.jp'
port = 80
request = "GET"
s.connect((server, port))
s.send(request.encode())
print("starting")
result = s.recv(4096)
s.close()
print(result.decode('UTF-8'))

