from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/test/<subject>', methods=['GET', 'POST'])
def test(subject):

    conn = sqlite3.connect("exam.db")
    c = conn.cursor()

    c.execute("SELECT * FROM questions WHERE subject=?", (subject,))
    questions = c.fetchall()

    score = 0

    if request.method == 'POST':

        for q in questions:

            user_answer = request.form.get(str(q[0]))

            correct_answer = q[6]

            if user_answer == correct_answer:
                score += 1

        return render_template(
            "result.html",
            score=score,
            total=len(questions)
        )

    return render_template(
        "test.html",
        questions=questions,
        subject=subject
    )


@app.route('/chat', methods=['GET', 'POST'])
def chat():

    reply = ""

    if request.method == 'POST':

        user_message = request.form['message'].lower()

        if user_message == "hello":
            reply = "Hi! I am NEA AI."

        elif user_message == "how are you":
            reply = "I am fine."

        elif user_message == "physics":
            reply = "Physics is interesting."

        elif user_message == "math":
            reply = "Math improves logical thinking."

        elif user_message == "bye":
            reply = "Goodbye!"

        else:
            reply = "I don't understand yet."

    return render_template(
        "chat.html",
        reply=reply
    )


if __name__ == '__main__':
    app.run(debug=True)
