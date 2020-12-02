from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app = Flask(__name__)
app.config['SECRET_KEY']="section193"

debug = DebugToolbarExtension(app)

responses = []
qid = str(len(responses))

@app.route('/')
def survey_home():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('home.html', title=title, instructions=instructions)

@app.route('/questions/0')
def que0():
    questions = satisfaction_survey.questions
    return render_template('question0.html', questions=questions)

@app.route('/questions/1', methods=['POST'])
def que1():
    answer = request.form['choice']
    responses.append(answer)
    questions = satisfaction_survey.questions
    return render_template('question1.html', questions=questions)

@app.route('/questions/2', methods=['POST'])
def que2():
    answer = request.form['choice']
    responses.append(answer)
    questions = satisfaction_survey.questions
    return render_template('question2.html', questions=questions)

@app.route('/questions/3', methods=['POST'])
def que3():
    answer = request.form['choice']
    responses.append(answer)
    questions = satisfaction_survey.questions
    return render_template('question3.html', questions=questions)

@app.route('/end', methods=['POST'])
def end():
    answer = request.form['choice']
    responses.append(answer)

    return render_template('end.html', responses=responses)

