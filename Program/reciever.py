import socket
import threading


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("not connect")
s.connect(("10.136.131.23", 3000))
print("Connected?")
msg = s.recv(1024)
print(msg.decode("utf-8"))
print("hello")

