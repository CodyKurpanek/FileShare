from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':   
        return render_template('index.html', profile = request.base_url + "account/" + request.form['username'])
    if request.method == 'GET':
        username = None
        return render_template('index.html', profile = username)



@app.route('/account/<username>')
def profile(username = None):
    return render_template('profile.html', username = username)
