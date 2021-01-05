from flask import Flask, render_template, abort, request, jsonify
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__

output = {}

def sentiment(sentence):

    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(sentence)['compound']
    if(score>0):
        return "Positive"
    else:
        return "Negative"

@app.route("/", methods = ["GET","POST"])
def request():
    if request.method == "POST":
        sentence = request.form["sentiment_input"]
        sentiment = sentiment(sentence)
        output['sentiment'] = sentiment
        return jsonify(output)
    else:
        sentence = request.args.get('sentiment_input')
        sentiment = sentiment(sentence)
        print(sentiment)
        output['sentiment'] = sentiment
        return {output}

app.run(debug=True)