from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app = Flask(__name__)
app.config['SECRET_KEY']="section193"

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False


@app.route('/')
def survey_home():
    
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('home.html', title=title, instructions=instructions)

@app.route('/new-user', methods=['POST'])
def new_user():
    session['responses'] = []
    return redirect('/questions/0')

@app.route('/questions/0')
def que0():
    questions = satisfaction_survey.questions
    return render_template('question0.html', questions=questions)

@app.route('/answers', methods=['POST'])
def store_answer():
    responses = session['responses']
    answer = request.form['choice']
    responses.append(answer)
    session['responses'] = responses

    qid = len(responses)

    return redirect(f"/questions/{len(responses)}")

@app.route('/questions/<int:qid>')
def display_que(qid):
    responses = session['responses']
    print(session['responses'])
    questions = satisfaction_survey.questions
    if (responses is None):
        return redirect("/")
        
    if (len(responses) != qid):
        flash("Error: you are trying to access question out of order")
        return redirect(f"/questions/{len(responses)}")

    if qid == len(satisfaction_survey.questions):
        return redirect('/end')


    return render_template('question.html',questions=questions, que_num=qid)


@app.route('/end')
def end():
    responses = session['responses']
    return render_template('end.html', responses=responses)

