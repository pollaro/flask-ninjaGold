from flask import Flask, render_template, request, redirect, session
import random, os, datetime
app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def index():
    if session.has_key('money'):
        session['money'] = session['money'] + session['cash']
        pass
    else:
        session['money']=0
    return render_template('index.html')

@app.route('/money',methods=['POST'])
def money():
    rand = random.random()
    if request.form['building'] == 'farm':
        cash = round(rand*(10)+10)
        session['location'] = 'farm'
    elif request.form['building'] == 'cave':
        cash = round(rand*(5)+5)
        session['location'] = 'cave'
    elif request.form['building'] == 'house':
        cash = round(rand*(3)+5)
        session['location'] = 'house'
    elif request.form['building'] == 'casino':
        cash = round(rand*(100)-50)
        session['location'] = 'casino'
    session['cash'] = cash
    return redirect('/')

app.run(debug=True)
