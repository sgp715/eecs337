from flask import Flask, url_for, render_template


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("login.html")

@app.route('/recommended', methods=['GET'])
def recomended():
    return render_template("recommended.html")

@app.route('/home', methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/popular', methods=['GET'])
def popular():
    return render_template("popular.html")

@app.route('/business', methods=['GET'])
def business():
    return render_template("business.html")

@app.route('/sports', methods=['GET'])
def sports():
    return render_template("sports.html")

@app.route('/international', methods=['GET'])
def international():
    return render_template("international.html")

@app.route('/political', methods=['GET'])
def political():
    return render_template("political.html")

@app.route('/science', methods=['GET'])
def science():
    return render_template("science.html")

@app.route('/something_new', methods=['GET'])
def something_new():
    return render_template("something_new.html")




if __name__ == "__main__":
    app.run(debug=True)
