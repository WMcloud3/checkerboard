from flask import Flask, render_template
app = Flask(__name__)




@app.route('/')
def index():
    return render_template("index.html", x = 8, y = 8, color1 = "red", color2 = "black")

@app.route('/4')
def index1():
    return render_template("index.html", x = 4, y = 8, color1 = "red", color2 = "black")

@app.route('/<number1>/<number2>')
def index2(number1, number2):
    return render_template("index.html", x = int(number1), y = int(number2), color1 = "red", color2 = "black")









if __name__=="__main__":
    app.run(debug=True)

