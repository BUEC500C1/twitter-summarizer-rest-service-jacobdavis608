from flask import Flask, escape, request
from video import twitter_movie


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Twitter Summarizer!</h1><p>Welcome to the Twitter Summarizer .</p>"

@app.route('/api/get_twitter_summary', methods=['GET'])
def api_summary():
    if 'num_tweets' in request.args:
        num = int(request.args['num_tweets'])
    else:
        return "Error: No num_tweets field provided"

    twitter_movie.twitter_movie(num=num, tweepy_keys_path="../access.txt")
    return "You requested %s tweets" % num
    

if __name__ == "__main__":
    app.run()
    #num =5 
    #twitter_movie.twitter_movie(num=num, tweepy_keys_path="../access.txt")
    # request: http://127.0.0.1:5000/api/get_twitter_summary?num_tweets=5