from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "<p>Hello, Mo</p>"


@app.route('/aboute')
def hello():
  return 'Hello, aboute'


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
