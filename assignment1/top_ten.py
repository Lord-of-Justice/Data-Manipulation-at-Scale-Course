import sys
import json
from collections import Counter


def main():
    tweet_file = open(sys.argv[1])
    dictionary = {}
    for line in tweet_file:
        tweet = json.loads(line)
        if "entities" in tweet:
            entities = tweet["entities"]
            hashtags = entities["hashtags"]

            for hashtag in hashtags:
                text = hashtag["text"]
                if text in dictionary.keys():
                    dictionary[text] += 1.0
                else:
                    dictionary[text] = 1.0

    sortDictionary = Counter(dictionary)
    top_ten = sortDictionary.most_common(10)
    for hashtag in top_ten:
        print(hashtag[0] + " " + str(hashtag[1]))


if __name__ == '__main__':
    main()