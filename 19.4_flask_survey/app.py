from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app = Flask(__name__)
app.config['SECRET_KEY']="section193"

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False


@app.route('/')
def survey_home():
    return render_template('home.html', surveys=surveys)

@app.route('/new-user', methods=['POST'])
def new_user():
    session['responses'] = []
    session['survey'] = request.form['picked_survey']
    return redirect('/questions/0')

@app.route('/questions/0')
def que0():
    selected = surveys[session['survey']]
    title = selected.title
    instructions = selected.instructions
    que_list = selected.questions
    return render_template('question0.html', questions=que_list, title = title, instructions=instructions)

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
    selected = surveys[session['survey']]
    title = selected.title
    instructions = selected.instructions
    que_list = selected.questions


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


    return render_template('question.html',questions=que_list, title = title, instructions=instructions, que_num=qid)


@app.route('/end')
def end():
    responses = session['responses']
    return render_template('end.html', responses=responses)

