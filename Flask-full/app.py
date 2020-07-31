from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Apple Lurve'

@app.route('/user/<username>')
def user(username):
    return f'Hello there {username}'

if __name__ == "__main__":
    app.run(debug=True)
