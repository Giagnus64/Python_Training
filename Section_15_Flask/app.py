from flask import Flask, render_template

app = Flask(__name__)

posts = {
    0: {
        'title': 'Hello, world',
        'content': 'First BLOG'
    }
}

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts.get(post_id)
    if not post:
        return render_template('404.jinja2', message='Post not found')
    return render_template('post.jinja2', post=post)


@app.route('post/form')
def form():
    return render_template('create.jinja2')

if __name__ == '__main__':
    app.run(debug=True)
