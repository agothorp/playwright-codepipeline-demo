from flask import Flask, render_template, request

application = Flask(__name__)

@application.route("/")
def home():
    return render_template("index.html")

@application.route("/lookup", methods=["POST"])
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
    application.run(host="0.0.0.0", port=5000)