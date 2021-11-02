from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Factorial!'

@app.route('/factorial/<int:number>')                             
def factorial(number):
    fact = 1
    for i in range(1, number + 1):
        fact = fact * i
    return '%d' % fact


if __name__ == '__main__':
    app.run()

