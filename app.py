from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/lookup", methods=["POST"])
def lookup():

    postcode = request.form["postcode"].strip().upper()

    if postcode == "MK18 1RY":
        council = "Buckinghamshire Council"
    else:
        council = None

    return render_template(
        "result.html",
        council=council
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)