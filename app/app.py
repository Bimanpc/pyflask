# app.py

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Connect to SQLite database
conn = sqlite3.connect('blog.db')
cursor = conn.cursor()

# Create a table for blog posts
cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        content TEXT NOT NULL
    )
''')
conn.commit()

@app.route('/')
def index():
    # Fetch all posts from the database
    cursor.execute('SELECT id, title FROM posts')
    posts = cursor.fetchall()
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def view_post(post_id):
    # Fetch a specific post by ID
    cursor.execute('SELECT title, content FROM posts WHERE id = ?', (post_id,))
    post = cursor.fetchone()
    return render_template('post.html', post=post)

# Add new post
@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        cursor.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
        conn.commit()
        return redirect(url_for('index'))
    return render_template('add_post.html')

if __name__ == '__main__':
    app.run(debug=True)
