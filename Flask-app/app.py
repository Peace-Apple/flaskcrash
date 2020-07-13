from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db' # tell the flask app where the database is stored relative /// absolute ////
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post' + str(self.id)

all_posts = [
    {
        'title': 'Post1',
        'content': 'This is the first post',
        'author': 'Apple'
    },
    {
        'title': 'Post2',
        'content': 'This is the second post'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    return render_template('posts.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
