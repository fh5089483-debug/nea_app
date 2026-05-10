from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""

    if request.method == "POST":

        question = request.form["question"].lower()

        if "salah" in question:
            answer = "Salah is the Islamic prayer performed five times daily."

        elif "quran" in question:
            answer = "The Quran is the holy book of Islam."

        elif "allah" in question:
            answer = "Allah is the Arabic word for God."

        else:
            answer = "Sorry, I am still learning."

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run()
