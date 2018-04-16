from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello'


if __name__ == '__main__':
    app.run(host='localhost',
            port=8686,
            debug=True)
