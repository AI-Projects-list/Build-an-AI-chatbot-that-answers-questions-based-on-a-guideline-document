from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    if request.method == "POST":
        msg = request.form["message"]
        r = requests.post("http://127.0.0.1:5000/chat", json={"message": msg})
        answer = r.json()["reply"]
    return render_template("index.html", reply=answer)

if __name__ == "__main__":
    app.run(debug=True)