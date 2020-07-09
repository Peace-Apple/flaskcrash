from flask import Flask, render_template, request, jsonify, flash
import random

app = Flask(__name__)
app.secret_key = b'am_very_secret'

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

@app.route('/math_game', methods=['GET', 'POST'])
def math_game():
    if request.method == 'POST':
        # handle correct /incorrect answer
        if 'answer' in request.form and 'correct_answer' in request.form:
            if request.form['answer'] == request.form['correct_answer']:
                flash('Correct!')
            else:
                flash(f"Incorrect! The correct answer was { request.form['correct_answer']}")
        # return jsonify(request.form)
        # pass

    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    correct_answer = num1 + num2
    return render_template('math.html', num1=num1, num2=num2, correct_answer=correct_answer)