# Sentiment Analysis Flask API
This sentiment analysis API allows you to get Sentiment for a sentence using GET and POST methods.

## Requirements
Use these or any latest  version if you already have installed.
    Flask==1.1.1
    nltk==3.4.5

## Usage
Using GET method - 

    http://127.0.0.1:5000?q="Text String to check Sentiment."
Using POST method - 

    curl http://127.0.0.1:5000 -d "q='Text String to check Sentiment.'"
or use in a web based form and send POST request.
## Output
Output is JSON based which is as follows -

    {"sentiment":"Negative"}
or

    {"sentiment":"Positive"}
