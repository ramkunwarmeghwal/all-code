#from crypt import methods
# from crypt import methods
from flask import Flask, render_template, request

# from a import MinSize
# from e import MaxSize

app = Flask(__name__)

# Pass the required route to the decorator.
@app.route("/second",methods=('post','get'))
def second():
   username = request.form['exampleList']
   MinSize = request.form['minsize']
   MaxSize = request.form['maxsize']

   return("username is"  + "MinSize" + "MaxSize")

    #return (render_template('e.html'))
	#return "Hello, Welcome to GeeksForGeeks"
	
@app.route("/",methods=["GET","POST"])
def index():
     return (render_template('test1.html'))
	#return "Homepage of GeeksForGeeks"

if __name__ == "__main__":
	app.run(debug=True)
