from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("exam.db")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test/<subject>', methods=['GET', 'POST'])
def test(subject):
    conn = get_db()
    c = conn.cursor()

    c.execute("SELECT * FROM questions WHERE subject=?", (subject,))
    questions = c.fetchall()

    if request.method == 'POST':
        score = 0
        for q in questions:
            qid = str(q[0])
            if request.form.get(qid) == q[6]:
                score += 1
        return render_template('result.html', score=score, total=len(questions))

    return render_template('test.html', questions=questions, subject=subject)

if __name__ == "__main__":
    app.run()
