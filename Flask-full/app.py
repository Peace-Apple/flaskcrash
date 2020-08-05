from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Apple Lurve' #context variable
    return render_template('index.html', name=name)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

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
