from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# your code here!
@app.route("/")
def hello():
    return render_template("index.template.html")
    
@app.route("/say-hello",methods=['POST'])
def processHello():
    firstname = request.form.get('first-name')
    lastname = request.form.get('last-name')
    return render_template('process-hello.template.html',fn=firstname,ln=lastname)


# this route handles both GET and POST
@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'GET':
        return render_template('calculate.html')
    elif request.method == 'POST':
        n1 = int(request.form.get('n1'))
        n2 = int(request.form.get('n2')) 
        total = n1+n2
        return render_template('show_result.template.html',answer=total)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)