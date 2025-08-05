# import python library packages

import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument("--light", action="store_true")
group.add_argument("--dark", action="store_true")

args = parser.parse_args()

if args.light:
    print("May force be with you.")
else:
    print("join me, and together we can rule the galaxy as father and son")

