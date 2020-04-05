import sys
import json
import re


def main():
    tweet_file = open(sys.argv[1])
    allTermsInTweets = 0
    dictionary = {}
    for line in tweet_file:
        tweet = json.loads(line)
        if "text" in tweet:
            text = tweet["text"]
            text = text.rstrip("\n")
            wordsInText = re.split(r"[\s\.\,\?\:\!\n]+", text)
            allTermsInTweets += len(wordsInText)

            for word in wordsInText:
                if word in dictionary and word != '':
                    dictionary[word] += 1.0
                elif word != '':
                    dictionary[word] = 1.0

    for word in dictionary.keys():
        print(word + " " + str(round(dictionary[word]/allTermsInTweets, 4)))


if __name__ == '__main__':
    main()