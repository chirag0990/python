#import python libraries

import argparse

parser = argparse.ArgumentParser(allow_abbrev=False, fromfile_prefix_chars="@")

parser.add_argument("item")
parser.add_argument("place")
parser.add_argument("description")
parser.add_argument("count")
parser.add_argument("--upper", action="store_true")

args = parser.parse_args()

text = f""" Magic {args.item} on the {args.place}, who is the {args.description} {args.count} of all?"""

if args.upper:
    text = text.upper()