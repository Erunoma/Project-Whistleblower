import socket

debug=True

def init_data():
    sid=0
    
    
def send_data():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.connect(("10.136.131.23", 3000))

    dataIWantToSend="Hello server"
    s.send(dataIWantToSend.encode())

    msg = s.recv(1024).decode("utf-8")
    print(msg)

if debug==True:
    init_data()
    send_data()
    
"""
while True:
    serversocket, address = s.accept()
    print(f"Connection from {address} has been established")
    stringToSend="Your call has also been recieved."
    serversocket.send(stringToSend.encode())
    
    
    
    
    
     
        s.connect()
        msg = s.recv(1024)
        print(msg.decode("utf-8")) 
 
"""