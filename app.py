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
    english = spacy.load("en_core_web_sm")
    result = english(st)
    sentences = [str(s) for s in result.sents]
    analyzer = vaderSentiment.SentimentIntensityAnalyzer()
    sentiment = [analyzer.polarity_scores(str(s)) for s in sentences]
    res=''
    res+="The statement you just entered is: \n"
    res+=st
    
    if(sentiment[0]['compound'] >= 0.05) : 
        sent="Positive " 
        emoji=128512
        address=' '
    elif(sentiment[0]['compound'] <= - 0.05) : 
        sent="Negative "
        emoji=128577
        address=' '
        
    else :
          sent="Neutral "
          emoji=128528
          address=' '
    res+="    OVERALL SENTIMENT: "+sent
   

    
    return render_template('output.html', sentences=st, sent=sent,emoji=emoji, address=address)
    

@app.route('/<s>')
def result(s):
    return f'<h1>You just navigated for: {s}</h1>'
    
if __name__ == '__main__':
    app.run(debug=True)