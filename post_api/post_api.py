from flask import Flask, render_template, request, redirect

app = Flask(__name__)

##http://127.0.0.1:5000/test

@app.route('/test')
def post1():
    return render_template('post.html')

##http://127.0.0.1:5000/calculate

@app.route('/calculate', methods=['POST'])
def post2():
    a = request.form['a']
    b = request.form['b']
    a_plus_b = int(a) + int(b)
    return render_template('add.html', c=a_plus_b)


if __name__ == '__main__':
    app.run()
