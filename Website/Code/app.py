
from flask import Flask, render_template, request
import sys
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3 
from flask import g




app = Flask("testapp")

#Mode modules
localMode=False
debugMode=False
dbTestMode=True
createNewTable=False

imported_id = 0
imported_lotCor = 0.0
imported_latCor= 0.0
imported_macAdd = "0.0.0.0.0.0"
imported_dateTime= "2/3"

whistlebase = sqlite3.connect('whistlebase.db', check_same_thread=False)





def create_table():
    cur = whistlebase.cursor()
    cur.execute("CREATE TABLE log (id int primarykey, lotCor float, latCor float, macAdd string, datetime string)")
    whistlebase.commit()
    print("A new table has been created")

def add_db_data():
    cur = whistlebase.cursor()
    cur.execute("INSERT INTO log (id, lotCor, latCor, macAdd, datetime) VALUES (?, ?, ?, ?, ?)",
            (imported_id, imported_lotCor, imported_latCor, imported_macAdd, imported_dateTime))
    
    whistlebase.commit()
    print("new log has been added")

def get_db_connection():
    conn = sqlite3.connect('whistlebase.db')
    conn.row_factory = sqlite3.Row
    print("Connection established to db")
    return conn
    
def clear_db():
    cur = whistlebase.cursor()
    cur.execute("DELETE FROM log")
    whistlebase.commit
    print("database has been cleared")

if createNewTable == True:
    create_table()

if dbTestMode == True:
    clear_db()
    add_db_data()
    add_db_data()
    get_db_connection()

    


#https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application
#https://flask.palletsprojects.com/en/2.2.x/patterns/sqlite3/
#The main site. Here is code for a button that, when pushed, "Posts" to the server, and runs the code associated
#with the button. 
@app.route("/", methods=["GET", "POST"])
def main():
    

#https://pythonbasics.org/flask-sqlite/
    if request.method== "POST":
        if request.form["action1"] == "GPS":
            lon=55.687101712605624
            lan=12.613155975026007
            gogurl="https://www.google.com/maps/search/?api=1&query="+str(lon)+","+str(lan)
            return render_template("gps.html",links=gogurl)
        if request.form["action1"] == "Database":
            whistlebase.row_factory = sqlite3.Row
            cur = whistlebase.cursor()
            db_show = cur.execute("SELECT * FROM log").fetchall()
            cur.close()
            return render_template("database.html", db_show=db_show)
        
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
        app.run(host="0.0.0.0", port=80)
elif debugMode==True:
    if __name__=="__main__":
        app.run(host="127.0.0.1", port=5000, debug=True)
else:
    if __name__=="__main__":   
      
        app.run(host="127.0.0.1", port=5000)    

#https://stackoverflow.com/questions/17309889/how-to-debug-a-flask-app





