from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/test', methods=['POST'])
def post():
    a = request.form['a']
    b = request.form['b']
    return a+b


@app.route('/test')
def post():
    return render_template('post.html')


if __name__ == '__main__':
    app.run()
