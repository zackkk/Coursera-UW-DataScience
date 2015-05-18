"""
Compute the sentiment of each tweet based on the sentiment scores (AFINN-111.txt) of the terms in the tweet. 
The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet.

The file AFINN-111.txt contains a list of pre-computed sentiment scores. 
Each line in the file contains a word or phrase followed by a sentiment score. 
Each word or phrase that is found in a tweet but not found in AFINN-111.txt should be given a sentiment score of 0. 
See the file AFINN-README.txt for more information.

$ python tweet_sentiment.py AFINN-111.txt output.txt   # output.txt is the input txt file
"""

import sys

def hw():
    print ('Hello, world!')

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()