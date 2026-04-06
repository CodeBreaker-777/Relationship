from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/7-november")
def nov7():
    return render_template("7_nov.html")

@app.route("/our-story")
def story():
    return render_template("story.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
