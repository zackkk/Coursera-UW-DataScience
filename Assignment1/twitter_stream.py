"""
Input: Url "https://stream.twitter.com/1/statuses/sample.json"
Output its twitter stream 

Explanation:
    Dependencies:
        oauth2 library: https://pypi.python.org/pypi/oauth2/
        Twitter credentials: https://apps.twitter.com/
    $ python twitterstream.py > output.txt
"""

import oauth2 as oauth
import urllib2 as urllib

"""
Global variables
"""
# See assignment1.html instructions or README for how to get these credentials
API_KEY = "KDuq3rWyUOYKLner9O1kofhFg"
API_SECRET = "AuhoGjioerjcEaFyS6XkkEC4wwjJVewJY3Lw8Ai43OR1d5aHeg"
ACCESS_TOKEN_KEY = "3198827438-Opdf2u9HqqRI8W4dKNFQicnvcg6VGslQ0FRjOVq"
ACCESS_TOKEN_SECRET = "05PRBuziXV3HRsTUFODjnxzUNTnCn3PXuXvzT9IbduBic"

_debug = 0
oauth_consumer = oauth.Consumer(key = API_KEY, secret = API_SECRET)
oauth_token    = oauth.Token(key = ACCESS_TOKEN_KEY, secret = ACCESS_TOKEN_SECRET)
signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()
http_method = "GET"
http_handler  = urllib.HTTPHandler(debuglevel = _debug)
https_handler = urllib.HTTPSHandler(debuglevel = _debug)

"""
Construct, sign, and open a twitter request
using the hard-coded credentials above.
"""
def twitter_request(url, method, parameters):
    request = oauth.Request.from_consumer_and_token(oauth_consumer,
                                            token = oauth_token,
                                            http_method = http_method,
                                            http_url = url, 
                                            parameters = parameters)
    request.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)
    headers = request.to_header()

    if http_method == "POST":
        encoded_post_data = request.to_postdata()
    else:
        encoded_post_data = None
        url = request.to_url()

    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)

    response = opener.open(url, encoded_post_data)
    return response

"""
Module starts here
"""
def fetch_samples():

    # tweet search API: https://dev.twitter.com/rest/reference/get/search/tweets
    # e.g.:url = "https://api.twitter.com/1.1/search/tweets.json?q=microsoft"

    url = "https://stream.twitter.com/1/statuses/sample.json"
    parameters = []
    response = twitter_request(url, "GET", parameters)
    for line in response:
        print line

    if __name__ == '__main__':
        fetch_samples()