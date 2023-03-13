from flask import Flask, render_template

app = Flask("testapp")

#Mode modules
localMode=True
debugMode=False

#Variables
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

#Hosting code. If localMode is False, the site will be hosted on the network. 
#Make sure to only disable localMode on safe networks.
#If debug mode is enabled, the site will be hosted locally in debug mode.
if localMode==False:
    if __name__=="__main__":
        app.run(host="0.0.0.0", port=80)
elif debugMode==True:
    app.run(host="127.0.0.1", port=5000, debug=True)
else:   
    app.run(host="127.0.0.1", port=5000)    

#https://stackoverflow.com/questions/17309889/how-to-debug-a-flask-app
