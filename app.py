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
    
    
    if(sentiment[0]['compound'] >= 0.05) : 
        sent="Positive " 
        emoji=128512
        address=' https://st.depositphotos.com/1016482/2236/i/950/depositphotos_22362437-stock-photo-background-with-heap-of-yellow.jpg'
    
    elif(sentiment[0]['compound'] <= - 0.05) : 
        sent="Negative "
        emoji=128577
        address='https://www.ecopetit.cat/wpic/mpic/270-2706765_sad-emoji-cover-photo-for-fb.jpg '
        
    else :
          sent="Neutral "
          emoji=128528
          address='https://atlas-content-cdn.pixelsquid.com/stock-images/neutral-face-facial-expression-L63Mrq1-600.jpg '
    
    
    return render_template('output.html', sentences=st, sent=sent,emoji=emoji, address=address)
    

@app.route('/<s>')
def result(s):
    return f'<h1>You just navigated for: {s}</h1>'
    
if __name__ == '__main__':
    app.run(debug=True)
