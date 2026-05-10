from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyB8GgP4Wg0rX7fPgfiqWBbMj4FuhSZO7Uw")

model = genai.GenerativeModel("gemini-pro")

@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""

    if request.method == "POST":

        question = request.form["question"]

        prompt = f"""
        You are an Islamic AI assistant.

        Answer respectfully.
        Use simple language.
        Answer Islamic questions carefully.

        User question:
        {question}
        """

        response = model.generate_content(prompt)

        answer = response.text

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run()
