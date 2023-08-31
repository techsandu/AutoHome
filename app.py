from flask import Flask
from electricity import electric


app = Flask(__name__)
app.register_blueprint(electric)

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!'


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=4040)
