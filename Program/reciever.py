import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.136.131.23", 3000))
msg = s.recv(1024)
print(msg.decode("utf-8"))

