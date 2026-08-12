from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/home_page")
def home_page():
    return "Home Page"

@app.route("/about")
def about():
    return "About Page"

@app.route("/contact")
def contact():
    return "Contact Page"

if __name__ == "__main__":
    app.run()