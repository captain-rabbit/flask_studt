from flask import Flask,render_template



app = Flask(__name__)


@app.route("/index")
def index():
    return render_template('home.html')


@app.route("/home")
def home():
    return "ok"

@app.route("/home1")
def home():
    return "ok"

if __name__ == '__main__':
    app.run()
    
