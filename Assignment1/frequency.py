"""
Input: tweet file
Output: term frequency

Explanation:
    frequency = [# of occurrences of the term in ALL tweets]/[# of occurrences of ALL terms in ALL tweets]

Example:
    $python frequency.py input.txt
"""

import collections
import re # regular expression
import sys

term_dictionary = {}
words_count = 0

def parse_tweet_file(tf):
    # Iterate all tweets in the file
    for line in tf:
        global words_count # when changing a variable, keyword global could avoid ambiguity
        words = re.findall("[a-z]+", line) # regular expression find all words
        for word in words:
            words_count += 1
            if word in term_dictionary:
                term_dictionary[word] += 1
            else:
                term_dictionary[word] = 1

def print_items():
    sorted_items = collections.OrderedDict(sorted(term_dictionary.items()))
    for key in sorted_items:
        print '(', key, ',', sorted_items[key] , '/' , words_count, ')'

def main():
    tweet_file = open(sys.argv[1])
    parse_tweet_file(tweet_file)
    print_items()

if __name__ == '__main__':
    main()