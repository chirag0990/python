# import package library

# import argparse

# parser = argparse.ArgumentParser()

# parser.add_argument("-w","--word", type=str, action="store",nargs=3)

# args = parser.parse_args()

# print(f"you want to ask your question: {args.word[0]}")
# print(f"you will get the answer: {args.word[1]}.")

### Example 2: 

# import argparse

# parser = argparse.ArgumentParser()

# parser.add_argument("tee", action="store", nargs="*", type=int)

# args = parser.parse_args()

# for x in range(10,0,-1):
#     if x in args.tee:
#         print("T-miuns", end=" ")
#     else:
#         print(x)

# print("Liftoff!")


# Example 3:

import argparse

SENTENCES = ["Listen to them.", "Childern of the night.", "What music they make."]

parser = argparse.ArgumentParser()
parser.add_argument("noise", action="store")
parser.add_argument("extra", action="store", nargs=argparse.REMAINDER)

args = parser.parse_args()

for sentence in SENTENCES:
    print(sentence,f"*{args.noise}* ", end=" ")

print()

print(" ".join(args.extra))


