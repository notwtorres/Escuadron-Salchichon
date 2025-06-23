from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    numbers = list(range(7))  
    random.shuffle(numbers)   # Los desordena
    return render_template("index.html", numbers=numbers)

if __name__ == "__main__":
    app.run(debug=True)
