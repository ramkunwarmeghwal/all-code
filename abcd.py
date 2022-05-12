#from crypt import methods
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    return (render_template('abcd.html'))

@app.route('/second', methods=['POST','GET'])
def second():
    username = request.form['username']   
    password = request.form['password']

    if username=="root" and password=="redhat":
        return (render_template('l.html'))
    else:
        return(render_template('abcd.html'))
         
    #return ("done")

if __name__ == '__main__':
      app.run(debug=True)