from flask import Flask, render_template, redirect

app = Flask(__name__)

#To open a Hello World HTML page
@app.route("/")
def main():
	return render_template('index.html')

#To open an HTML page on click of button from the current page
@app.route("/next", methods=['POST'])
def next():
	return render_template('next.html')

#To go back to home page
@app.route("/index", methods=['POST'])
def home():
	return render_template('index.html')

# Shows a random page with the "message" entered by the user in the URL	
@app.route("/<message>")
def show_message(message):
	return "Hello World ! %s"%message

# Goes back to the home page if URL is different from any of the above
@app.errorhandler(404) 
def page_not_found(e): 
	return redirect('/')
	
if __name__=="__main__":
	app.run()