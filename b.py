from crypt import methods
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    return (render_template('test.html'))

# @app.route('/second', methods=['POST','GET'])
# def second():
#     text = request.form['stars']
#     minsize = request.form['minsize']
#     maxsize = request.form['minsize']   
    
#     return ("done")

if __name__ == '__main__':
      app.run()