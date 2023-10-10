from flask import Flask, render_template

import animator 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/plots/<int:value>')
def plots(value):
    if value == 1:
        return animator.plot('CV 0.5.txt')
    elif value == 2:
        return animator.plot('CV 0.75.txt')

if __name__ == '__main__':
    app.run(debug = True)