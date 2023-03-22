
from flask import Flask, render_template, request
import sys
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask("testapp")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///whistlebase.db'
#initilize database
db = SQLAlchemy(app)

class Whistlebase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lotCor = db.Column(db.Float)
    latCor = db.Column(db.Float)
    macAdd = db.Column(db.String(200))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, id, lotCor, latCor ,macAdd, date_added):
        self.id = id
        self.lotCor = lotCor
        self.latCor = latCor
        self.macAdd = macAdd
        self.date_added = date_added

#Mode modules
localMode=True
debugMode=False

#Variables


#URL's


#The main site. Here is code for a button that, when pushed, "Posts" to the server, and runs the code associated
#with the button. 
@app.route("/", methods=["GET", "POST"])
def main():

    if request.method== "POST":
        if request.form["action1"] == "GPS":
            lon=55.687101712605624
            lan=12.613155975026007
            gogurl="https://www.google.com/maps/search/?api=1&query="+str(lon)+","+str(lan)
            return render_template("gps.html",links=gogurl)
        if request.form["action1"] == "Database":
            return render_template("database.html")
        if request.form["action1"] == "Profiles":
            return render_template("profiles.html")
         
    elif request.method == "GET":
        return render_template("main.html")



with app.app_context():
      print("Database created")
      db.create_all()


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

"""
    #To output a variable to the server, the variable needs to be sent to the HTML document
    #in the render_template section
    return render_template("main.html", appTestVar=connect.testVar)
"""