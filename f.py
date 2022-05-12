import re
from unicodedata import name
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
     return render_template('base.html')

@app.route('/friends/<name>')
def friend(name):
     return render_template('friends.html',name=name)   


@app.route('/',methods=("POST", "GET"))
def asg():
    return ("I already Clicked !!", 'base.html')     
       



#def hello_world():
 #   return '<h1>Hello world! </h1>'

#@app.route('/info')
#def info():
 #   return '<h1>Information Page! </h1>'

#@app.route('/friend/<name>')
#def friend(name):
 #   return '<h1>Last word of name {}</h1>'.format(name[-1])

if __name__=='__main__':
    app.run(debug=True)