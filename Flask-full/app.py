from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<username>')
def user(username):
    return f'Hello there {username}'

# How to work with cookies

@app.route('/set')
def setCookie():
    response = make_response('I have set the cookie')
    response.set_cookie('myapp', 'Flask Development')

    return response

@app.route('/get')
def getCookie():
    myapp = request.cookies.get('myapp')
    return 'Cookie content ' + str(myapp)

if __name__ == "__main__":
    app.run(debug=True)
