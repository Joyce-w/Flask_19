from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app = Flask(__name__)
app.config['SECRET_KEY']="section193"

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def survey_home():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('home.html', title=title, instructions=instructions)