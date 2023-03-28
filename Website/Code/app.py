
from flask import Flask, render_template, request # Imports flask-module 
import sys
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3 
from flask import g
import socket 
from threading import Thread
import threading


# Creates flask-app names "testapp"
app = Flask("testapp")

#Mode modules
localMode=False
debugMode=False
dbTestMode=True
createNewTable=False

isDatabaseBusy = False

# Assign variables, create the global variable "sentdata" and assign it to an empty list  
imported_id = 0
imported_lotCor = 0.0
imported_latCor= 0.0
imported_macAdd = "0.0.0.0.0.0"
imported_dateTime= "2/3"
global sentdata
sentdata=[]

# the name "whistlebase" gets assigned to an sqlite3-connection to a database called "whistlebase.db". Therefore, refering to the connection is now "whistlebase".  
whistlebase = sqlite3.connect('whistlebase.db', check_same_thread=False)

# A function used for creating a table in the database. Takes 5 args listed in the (). Makes a commit with the listed fields to the database and afterwards, prints "A new table has been created". 
def create_table():
    cur = whistlebase.cursor()
    cur.execute("CREATE TABLE log (id int primarykey, lotCor float, latCor float, macAdd string, datetime string)")
    whistlebase.commit()
    print("A new table has been created")

# A function used for inserting the 5 given args listed above into the database with the collected data. After doing the commit, prints "new log has been added" 
def add_db_data():
    global imported_id
    global imported_lotCor
    global imported_latCor
    global imported_macAdd
    global imported_dateTime
    cur = whistlebase.cursor()
    cur.execute("INSERT INTO log (id, lotCor, latCor, macAdd, datetime) VALUES (?, ?, ?, ?, ?)",
            (imported_id, imported_lotCor, imported_latCor, imported_macAdd, imported_dateTime))
    
    whistlebase.commit()
    print("new log has been added")

# A function used to check for connection to the db. 
def get_db_connection():
    conn = sqlite3.connect('whistlebase.db')
    conn.row_factory = sqlite3.Row
    print("Connection established to db")
    return conn

# Function used to clear the log in the database. Executes the clear by doing a commit. Afterwards, prints "database has been cleared".    
def clear_db():
    cur = whistlebase.cursor()
    cur.execute("DELETE FROM log")
    whistlebase.commit
    print("database has been cleared")

# If-statements checking the variables in the top of the script. If the condition is True, a function is called. Goes for both if-statements seen below. 
if createNewTable == True:
    create_table()

if dbTestMode == True:
    clear_db()
    #add_db_data()
    #add_db_data()
    get_db_connection()

# a function creating the socket for the website. Binds on port 3000 on local network. If connection is established and listening, a condition evaluates to True.
# If so, data is sent to and recieved by the database assigning it to the variable "newSentData" The sent data is decoded to utf-8-format and splitted.  
# At the end of the function, the connection is closed. 
def init_socket():
    global s
    global newSentData

    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("", 3000))
    print("Listening...")
    s.listen()
    while True:
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established")
        stringToSend="Your call has been recieved."
        sentdata= [str(i) for i in clientsocket.recv(2048).decode("utf-8").split("\n")]
        print(sentdata)
        newSentData = sentdata
        convert_and_apply()
        stringToSend="Data has been recieved."
        clientsocket.send(stringToSend.encode())
        s.close()
        init_thread()
      
# This function is used above when the data is converted. A print-function prints the data in convert. 
def convert_and_apply():
    global imported_id
    global imported_lotCor
    global imported_latCor
    global imported_macAdd
    global imported_dateTime
    global newSentData
    print("Converting...")
    print("This is the new sent data in convert : ",newSentData)

# Variable-names are assigned to values from the list with the name "newSentData". These variables also get converted into strings, floats and integers.
# A print with the data recieved is executed.
# The function add_db_data described above is called.
# An exeption is throwed if an error occurs. A print with the message "An error has occured" is shown. 
    try:
        imported_id = int(newSentData[0])
        imported_lotCor = float(newSentData[1])
        imported_latCor = float(newSentData[2])
        imported_macAdd = str(newSentData[3])
        imported_dateTime = str(newSentData[4])
        print(f"Data retrieved from device: \n {imported_id} \n {imported_lotCor} \n {imported_latCor} \n {imported_macAdd} \n {imported_dateTime} \n ")

        add_db_data()
    except Exception as e: print("An error has occured: ",e)
     

def init_thread():
    th = Thread(target=init_socket)
    th.start()
    th.join()
    print("New thread started")
        
       
#https://docs.python.org/3/library/socket.html#creating-sockets
#https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application
#https://flask.palletsprojects.com/en/2.2.x/patterns/sqlite3/
#The main site. Here is code for a button that, when pushed, "Posts" to the server, and runs the code associated
#with the button. 
@app.route("/", methods=["GET", "POST"])
def main():
#https://pythonbasics.org/flask-sqlite/
    if request.method== "POST":
        if request.form["action1"] == "GPS":
            lon=imported_lotCor
            lan=imported_latCor
            gogurl="https://www.google.com/maps/search/?api=1&query="+str(lon)+","+str(lan)
       
            return render_template("gps.html",links=gogurl)
        if request.form["action1"] == "Database":
            whistlebase.row_factory = sqlite3.Row
            cur = whistlebase.cursor()
            db_show = cur.execute("SELECT * FROM log").fetchall()
            cur.close()
            print(str(db_show))
            mapLinks=[]
            for log in db_show:
                mapLinks.append("https://www.google.com/maps/search/?api=1&query="+str(log["lotCor"])+","+str(log["latCor"]))
            print(mapLinks)
            return render_template("database.html", db_show=db_show, mapLinks=mapLinks)
        
        if request.form["action1"] == "Profiles":
            return render_template("profiles.html")
         
    elif request.method == "GET":
        return render_template("main.html")
    

#https://stackoverflow.com/questions/31965558/how-to-display-a-variable-in-html
#https://flask.palletsprojects.com/en/2.2.x/tutorial/templates/

#Hosting code. If localMode is False, the site will be hosted on the network. 
#Make sure to only disable localMode on safe networks.
#If debug mode is enabled, the site will be hosted locally in debug mode.
if localMode==False:
    if __name__=="__main__":
        th = Thread(target=init_socket)
        th.start()
        print("Thread startup")
        app.run(host="0.0.0.0", port=80)
        th.join()
        
        
elif debugMode==True:
    if __name__=="__main__":
        app.run(host="127.0.0.1", port=5000, debug=True)
        
else:
    if __name__=="__main__":   
        app.run(host="127.0.0.1", port=5000) 
   

#https://stackoverflow.com/questions/17309889/how-to-debug-a-flask-app


