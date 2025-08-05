# # import python package libraries

# import argparse

# # Action

# def raiders(args):
#     print(f"{args.animal.capitalize()}. Why'd it have to be {args.animal}?")

# def doom(args):
#     for _ in range(args.repeat):
#         print("Kali Ma.....")

#     print("Shakti Ma....")

# def crusade(args):
#     print(f"Sallah I said no caremal. That's '{args.count}' camels.")
#     print("Can't you count")

# #Parser

# parser = argparse.ArgumentParser()
# subparser = parser.add_subparsers(title="subcommands", dest="commands")
# subparser.required = True

# sub = subparser.add_parser("raiders")
# sub.add_argument("animal")
# sub.set_defaults(func=raiders)

# sub = subparser.add_parser("doom")
# sub.add_argument("-r", dest = "repeat", default=3, type=int, metavar="NUM")
# sub.set_defaults(func=doom)

# sub = subparser.add_parser("crusade")
# sub.add_argument("count")
# sub.set_defaults(func=crusade)

# # excuate 
# args = parser.parse_args()
# args.func(args)


import argparse

def multiply(a, b):
    return a * b

def create_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    multiply_parser = subparsers.add_parser("multiply")
    multiply_parser.add_argument("operands", type=float, nargs=2)
    multiply_parser.set_defaults(func=multiply)

    return parser