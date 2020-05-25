import spacy
from vaderSentiment import vaderSentiment
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')
    
@app.route('/',methods=['POST'])
def func():
    st=request.form["review"]
    return st
    

@app.route('/<s>')
def result(s):
    return f'<h1>You just navigated for: {s}</h1>'
    
if __name__ == '__main__':
    app.run(debug=True)