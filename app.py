from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route("/")
def index():
    url = "https://adorbs-as-a-service.herokuapp.com/api/v1/w300/h300?rounded=100"
    return render_template("index.html", url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
