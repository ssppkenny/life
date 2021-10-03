from game_of_life import *
from flask import Flask, render_template
app = Flask(__name__)
game = GameOfLife()
universe = game.world
app.game = game
app.universe = universe

@app.route("/live")
def live():
    game = app.game
    universe = game.world
    if not hasattr(game, 'counter'):
        game.counter = 0
    else:
        game.form_new_generation()
        game.counter += 1
    return render_template('live.html', game=app.game)

@app.route("/")
def main():
    return render_template('index.html')
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

 
