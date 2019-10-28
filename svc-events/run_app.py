from flask import Flask

application = Flask(__name__)


@application.route(rule='/hello')
def route_hello():
    return 'Hello!', 200
