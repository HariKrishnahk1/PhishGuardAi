from flask import Flask, render_template, request
from ai_analyzer import analyze_message

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    result = None

    if request.method == "POST":
        text = request.form["content"]
        result = analyze_message(text)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)