from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("phishing_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        url = request.form["url"]

        # Temporary sample features
        features = [[1, 1, 1, 1, 1]]

        prediction = model.predict(features)

        if prediction[0] == 1:
            result = "Legitimate Website"
        else:
            result = "Phishing Website"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)