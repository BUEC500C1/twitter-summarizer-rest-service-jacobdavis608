
# REST Service for Twitter Summary

## Assignment details
* Step 1: Use Flask as your WEB service platform
  * Reference 1:  https://palletsprojects.com/p/flask/ (Github:  https://github.com/pallets/flask )
  * Reference 2:  Flask-RESTFUL  (Github:  https://github.com/flask-restful/flask-restful )
* Step 2:  Integrate your module to become a RESTFUL system
* Deploy your system to free AWS services:  https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc
* Develop simple WEB applications to test your system.
* Document your REST APIs on your Github
* KEep your server off until we request it for grading.  We dont want you to waste money.


## API documentation and usage
To use the web api "mytwitterapi". This simple api implements a single get request response that returns an mp4 to the browser as an attachment. The user passes in the url a single parameter, num_tweets, that defines the number of tweets they want to get from the timeline.

An example request looks like this (please use this for testing):
      http://127.0.0.1:5000/api/get_twitter_summary?num_tweets=5

