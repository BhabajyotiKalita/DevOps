from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Welcome'

@app.route('/bhaba')
def bhaba():
    return 'Hello BK'

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')