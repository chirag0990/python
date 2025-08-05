# import library packages 

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("container", choices=["box", "carton"])
parser.add_argument("-r", dest="repeat", required=True, type=int, choices=range(1,6))
args = parser.parse_args()

for _ in range(args.repeat):
    print(f"Life is like a {args.container} of chocolates")

    