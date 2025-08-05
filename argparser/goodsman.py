# import library packages

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-s","--shout",action="count",default=0)
words = "You con't handle the truth!".split()

args = parser.parse_args()

for count, words in enumerate(words):
    if (count + 1) <= args.shout:
        print(words.upper() + " ", end=" ")
    else:
        print(words + " ", end=" ")
print()
