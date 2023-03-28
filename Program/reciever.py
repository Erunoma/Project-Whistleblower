import socket

debug=True

def init_data(deviceID, lot, lat ,macAdd, curTime):
    global newdata
    newdata=[deviceID, lot,lat, macAdd, curTime]
    print("added values")
    send_data()

    
def send_data():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.connect(("192.168.1.187", 3000))

    sentdata=newdata
    print(sentdata)
    s.sendall(str.encode("\n".join([str(sentdata[0]),str(sentdata[1]), str(sentdata[2]), str(sentdata[3]), str(sentdata[4])])))

    msg = s.recv(1024).decode("utf-8")
    print(msg)
    print("values sent")

if debug==True:
    init_data(29,55.671170,12.522459,"Mac adress goes here:", "10:30 3/1")
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