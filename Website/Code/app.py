from flask import Flask, render_template

app = Flask("testapp")

publicVar=0

@app.route("/")

def main():
    var=0
    var+=1
    #To output a variable to the server, the variable needs to be sent to the HTML document
    #in the render_template section
    return render_template("main.html", publicVar=var)


#https://stackoverflow.com/questions/31965558/how-to-display-a-variable-in-html
#https://flask.palletsprojects.com/en/2.2.x/tutorial/templates/






#To make the website viewable online, use this code in the terminal:
#$ flask run --host=0.0.0.0
