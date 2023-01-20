from flask import Flask, render_template

#Create flask instance

app = Flask(__name__)

#Create a rout decorator
@app.route('/')

#def index():
#	return "<h1> Hello World!</h1>"


#safe
#capitalize
#lower
#upper
#title
#trim
#striptage


def index():
	first_name = "John"
	stuff = "This is <b>Bold</b> text"
	favourite_pizza=["Pepperonoi", "Cheese", 41]
	return render_template("index.html", first_name=first_name, stuff=stuff, favourite_pizza=favourite_pizza)


#localhost:5000/user/john
@app.route('/user/<name>')

def user(name):
	return render_template("user.html",user_name=name)

#Custom error pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

#Internal server error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500

