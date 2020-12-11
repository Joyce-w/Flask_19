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

    return render_template("board.html", )


@app.route("/answers", methods=["GET"])
def get_answer():
    if request.method == "GET":
        #reterive json data from app.js POST
        word = request.args['submitted']

    #make sure word is valid on the board using check_valid_word() from boggle.py
    session_board = session['game_board']
    res = boggle_board.check_valid_word(session_board, word)
    result = {"result": res, "word":word}
    return jsonify(result)
 