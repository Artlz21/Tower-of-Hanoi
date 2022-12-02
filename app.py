from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        return redirect(url_for("gamePage"))
    else:
        return render_template('base.html')


@app.route('/game', methods = ["GET", "POST"])
def gamePage():
    PlayerScore = 99
    if request.method == "POST":
        return redirect(url_for("home", score=PlayerScore))
    else:
        return render_template('gamePage.html', InScore=PlayerScore)




if __name__ == "__main__":
    app.run(debug=True)

    '''    
@app.route('/GameOver/<nameEnd>/<score>')
def gameOver(nameEnd, score):
    return render_template('endGame.html', inNameEnd=nameEnd, inScore=score)
    '''

'''Testing retrieval 

@app.route('/<name>') 
def gamePage(name):
    return render_template('gamePage.html', result=name)'''

