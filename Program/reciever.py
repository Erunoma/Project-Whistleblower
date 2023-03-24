import socket

debug=True

def init_data(macAdd, curTime):
    global newdata
    
    newdata=[macAdd, curTime]
    
    print("added values")

    
def send_data():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.connect(("10.136.131.23", 3000))

    sentdata=newdata
    print(sentdata)
    s.sendall(str.encode("\n".join([str(sentdata[0]),str(sentdata[1])])))

    msg = s.recv(1024).decode("utf-8")
    print(msg)
    print("values sent")

if debug==True:
    init_data("Mac adress goes here:", "10:30 3/1")
    send_data()
    print("started debug")
    
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