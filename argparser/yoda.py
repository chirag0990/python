# import python libararies

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--try", dest="Try", action=argparse.BooleanOptionalAction)

args = parser.parse_args()

if args.Try:
    print("Do or Don't. Try it")
else:
    print("failed it")
    
        