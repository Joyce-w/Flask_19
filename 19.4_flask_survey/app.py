from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app = Flask(__name__)
app.config['SECRET_KEY']="section193"

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False


@app.route('/')
def survey_home():
    """Load home page,survey selection"""
    return render_template('home.html', surveys=surveys)

@app.route('/new-user', methods=['POST'])
def new_user():
    """Make session for specific user to store answers"""
    session['responses'] = []
    session['survey'] = request.form['picked_survey']
    return redirect('/questions/0')

@app.route('/questions/0')
def que0():
    """Display first question of the selected survey"""
    #save the survey obj of the selected survey, get the questions within
    selected = surveys[session['survey']]
    que_list = selected.questions

    #get title,insurctions of choosen survey
    title = selected.title
    instructions = selected.instructions

    return render_template('question0.html', questions=que_list, title = title, instructions=instructions)

@app.route('/answers', methods=['POST'])
def store_answer():
    """POST route to send answers and input into response"""
    answer = request.form['choice']
    comment = request.form.get('comment', "")

    #add response(s) to session
    responses = session['responses']
    responses.append({"choice":answer, "comment":comment})
    session['responses'] = responses

    return redirect(f"/questions/{len(responses)}")

@app.route('/questions/<int:qid>')
def display_que(qid):
    """Dynamic route to display corresponding question"""

    #save survey obj of selected survey
    selected = surveys[session['survey']]

    #save title and instruction of selected survey
    title = selected.title
    instructions = selected.instructions

    #select list of question within survey
    que_list = selected.questions

    responses = session['responses']
    questions = satisfaction_survey.questions

    #if manual redirected a question, redirect to home
    if (responses is None):
        return redirect("/")
    
    #if the response is the same as the length of subroute value, end survey, otherwise redurect to correct quesiton num
    if (len(responses) != qid):
        flash("Error: you are trying to access question out of order")
        return redirect(f"/questions/{len(responses)}")

    if qid == len(satisfaction_survey.questions):
        return redirect('/end')
    
    #render the question html
    return render_template('question.html',questions=que_list, title = title, instructions=instructions, que_num=qid)


@app.route('/end')
def end():
    """Ending route after survey completed"""
    responses = session['responses']
    return render_template('end.html', responses=responses)

