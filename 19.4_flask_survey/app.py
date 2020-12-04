from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app = Flask(__name__)
app.config['SECRET_KEY']="section193"

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False

responses = []

@app.route('/')
def survey_home():
    responses.clear()
    
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('home.html', title=title, instructions=instructions)

@app.route('/questions/0')
def que0():
    questions = satisfaction_survey.questions
    return render_template('question0.html', questions=questions)

@app.route('/answers', methods=['POST'])
def store_answer():
    answer = request.form['choice']
    responses.append(answer)
    qid = len(responses)
    survey_len = len(satisfaction_survey.questions)

    if qid == survey_len:
        return redirect('/end')
    else:
        return redirect(f"/questions/{len(responses)}")

@app.route('/questions/<int:qid>')
def display_que(qid):
    questions = satisfaction_survey.questions
    return render_template('question.html',questions=questions, que_num=qid)


@app.route('/end')
def end():
    
    return render_template('end.html', responses=responses)

