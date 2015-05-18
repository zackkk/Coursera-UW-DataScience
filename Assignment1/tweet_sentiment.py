"""
Input: sentiment computation file, tweet file
Output: sentiment score for each tweet

Explanation:
    Compute the sentiment of each tweet based on the sentiment scores (AFINN-111.txt, tab-delimited) of the terms in the tweet. 
    The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet.

    The file AFINN-111.txt contains a list of pre-computed sentiment scores. 
    Each line in the file contains a word or phrase followed by a sentiment score. 
    Each word or phrase that is found in a tweet but not found in AFINN-111.txt should be given a sentiment score of 0. 
    See the file AFINN-README.txt for more information.

    What information each tweet contains: https://dev.twitter.com/overview/api/tweets
    simplejson: https://pypi.python.org/pypi/simplejson/
        install: $python setup.py install

Example:
    $ python  tweet_sentiment.py  AFINN-111.txt  output.txt
    # output.txt is the input txt file name
"""

import json
import re # regular expression
import sys

sentiment_dictionary = {}
tweet_lines = {}

def is_json(js):
    try:
        json_object = json.loads(js)
    except ValueError, e:
        return False
    return True

def parse_sentiment_file(sf):
    for line in sf:
        term, score = line.split("\t")
        sentiment_dictionary[term] = int(score)

def parse_tweet_file(tf):
    # Iterate all tweets in the file
    for line in tf:

        #The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet
        sum = 0

        # Eliminate non-ascii and zero chars for json.loads
        line =  "".join(i for i in line if ord(i) < 128 and ord(i) > 0)

        if is_json(line) == True:
            words = re.findall("[a-z]+", line) # regular expression find all words
            for word in words:
                if word in sentiment_dictionary:
                    sum = sum + sentiment_dictionary[word]
        print sum

def main():
    sentiment_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    parse_sentiment_file(sentiment_file)
    parse_tweet_file(tweet_file)

if __name__ == '__main__':
    main()