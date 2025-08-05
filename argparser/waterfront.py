import argparse

parser = argparse.ArgumentParser()
parser.version = "1.0"
parser.add_argument("-w", "--word", type=str, action="append", help="Add a word to the list")
parser.add_argument("-?", action="help")
parser.add_argument("-v", "--version", action="version")

args = parser.parse_args()

print(f"you don't understand! I could had {args.word[0]}.")
print(f"you could've been a {args.word[1]}. I could've been")
print(f"{args.word[2]}, instead of a bum, which is what I am.")

