from flask import Flask
from flask import request

app = Flask(__name__)

## http://localhost:5000/?id=cheon&pw=seyoung

@app.route('/')
def user_login():
    temp = request.args.get('id', "username")
    temp1 = request.args.get('pw', "password")

    return 'id: %s pw: %s' % (temp, temp1)


if __name__ == "__main__":
    app.run()
