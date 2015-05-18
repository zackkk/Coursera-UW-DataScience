"""
input: sentiment computation file, tweet file
output: sentiment score for each tweet

Explanation:
    Compute the sentiment of each tweet based on the sentiment scores (AFINN-111.txt, tab-delimited) of the terms in the tweet. 
    The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet.

    The file AFINN-111.txt contains a list of pre-computed sentiment scores. 
    Each line in the file contains a word or phrase followed by a sentiment score. 
    Each word or phrase that is found in a tweet but not found in AFINN-111.txt should be given a sentiment score of 0. 
    See the file AFINN-README.txt for more information.

    What information each tweet contains: https://dev.twitter.com/overview/api/tweets

    $ python tweet_sentiment.py AFINN-111.txt output.txt   # output.txt is the input txt file
"""

import sys
import json

sentiment_dictionary = {}

def parse_sentiment_file(sf):
    for line in sf:
        term, score = line.split("\t")
        sentiment_dictionary[term] = int(score)

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sentiment_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    parse_sentiment_file(sentiment_file)
    

    print sentiment_dictionary.items()

if __name__ == '__main__':
    main()