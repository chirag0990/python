# import libarary packages
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--place", type=str)
parser.add_argument("-c", "--city", type=str, default="towns")
parser.add_argument("-v", "--verb", type=str)
parser.add_argument("-r", action="store_true", default=False)

args = parser.parse_args()

print(f" of all the {args.place} in all the {args.city}, in the world,")
print(f"she {args.verb} into mine")

if args.r:
    print("Here's looking at you, kid.")