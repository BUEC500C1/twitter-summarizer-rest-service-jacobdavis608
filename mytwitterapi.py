from flask import Flask, escape, request, make_response, send_file
from video import twitter_movie
from io import BytesIO
import zipfile
import time

app = Flask(__name__)
#app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Twitter Summarizer!</h1><p>Welcome to the Twitter Summarizer .</p>"

@app.route('/api/get_twitter_summary', methods=['GET'])
def api_summary():
    if 'num_tweets' in request.args:
        num = int(request.args['num_tweets'])
    else:
        return "<h1>Error:</h1><p>No num_tweets field provided, no specified movie length.</p>"

    twitter_movie.twitter_movie(num=num, tweepy_keys_path="../access.txt")
    out_path = './twitter_summary.mp4'
    return send_file(out_path, as_attachment=True)
    

if __name__ == "__main__":
    app.run()