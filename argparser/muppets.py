# import python package library

import argparse

class BorkAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs is not allowed")
        super(BorkAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string = None):
        result = values + " Bork, bork, bork!"
        setattr(namespace,self.dest,result)

parser = argparse.ArgumentParser()
parser.add_argument("quote", action=BorkAction)

args = parser.parse_args()

print(args.quote)


