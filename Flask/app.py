from flask import Flask, render_template
import random

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World my Apple'

# @app.route('/about')
# def about():
#     return 'I am a software developer'

# @app.route('/user/<username>')
# def user_profile(username):
#     return f'I am user {username}'

@app.route('/')
def home():
    return render_template('home.html', username='Apple Lurve')

@app.route('/math_game')
def math_game():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    return render_template('math.html', num1=num1, num2=num2)