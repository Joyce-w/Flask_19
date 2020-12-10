from boggle import Boggle
from flask import Flask, render_template, session, request, redirect, jsonify
from flask_debugtoolbar import DebugToolbarExtension
boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY']="195flasktesting"

debug = DebugToolbarExtension(app)

boggle_board = Boggle()

@app.route("/")
def home():
    
    board = boggle_board.make_board()
    session['game_board'] = board
    return render_template("board.html")


@app.route("/answers", methods=['POST'])
def get_answer():
    #reterive json data from app.js POST
    word = request.form['submitted']
    #save to seesion
    session['guess'] = word

    #make sure word is valid on the board using check_valid_word() from boggle.py
    session_board = session['game_board']
    validate = boggle_board.check_valid_word(session_board, word)
    #save to seesion
    session['result'] = validate

    return redirect("/")
