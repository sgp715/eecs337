from flask import Flask, url_for, render_template


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("login.html")

@app.route('/profile', methods=['GET'])
def profile():
    return render_template("profile.html")

@app.route('/recommended', methods=['GET'])
def recomended():
    return render_template("recommended.html")

@app.route('/home', methods=['GET'])
def home():
    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
