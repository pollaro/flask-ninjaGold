from flask import Flask, render_template, request, redirect, session
import random,os
app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)
