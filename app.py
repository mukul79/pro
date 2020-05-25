from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def hello():
    if(request.method=="POST"):
        s=request.args['review']
        return redirect(url_for('hello',s=s))
    else: 
        return render_template('index.html')
    
@app.route('/<usr>')
def result():
    return f'<h1>{usr}</h1>'
    
if __name__ == '__main__':
    app.run(debug=True)