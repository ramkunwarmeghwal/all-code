# from crypt import methods
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    return (render_template('form.html'))
    return (render_template('d.html'))
@app.route('/second', methods=['POST','GET'])
def second():
    text = request.form['Uname']
    password = request.form['Pass']  
    return (render_template('d.html'))
    return ("user name is :" + text + "and password is" + password)

if __name__ == '__main__':
      app.run(debug=True)