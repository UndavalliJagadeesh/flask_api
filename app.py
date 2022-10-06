from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'HOME'


@app.route('/super_simple')
def super_simple():
    return 'Hello from API'


if __name__ == '__main__':
    app.run()