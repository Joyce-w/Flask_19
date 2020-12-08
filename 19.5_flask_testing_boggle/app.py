from boggle import Boggle
from flask import Flask, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY']="195flasktesting"

debug = DebugToolbarExtension(app)


@app.route("/")
def home():
    boggle_board = Boggle()
    board = boggle_board.make_board()
    session['game_board'] = board
    return render_template("board.html", board=board)
