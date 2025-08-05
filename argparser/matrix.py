
# Help & postional and optional arguments
# To see the help message, run the script with -h or --help
# python arg_parse.py -h
# or
# python arg_parse.py --help

import argparse, string, random

TEXT = string.ascii_letters + string.digits + string.punctuation

parser = argparse.ArgumentParser(prog="matrix",
                                 usage="%(prog)s [options] numbers",
                                 description="prints random numbers of columns",
                                epilog="Enjoy the matrix")
parser.add_argument("num",type=int)

# porg parameter we used to change the name of the program in the help message, 
# without this, the name will be the full matrix.py

# description parameter is used to provide a brief description of the program,
# epilog parameter is used to provide a message at the end of the help message

args = parser.parse_args()

for _ in range(args.num):
    content = [random.choice(TEXT) for _ in range(20)]
    print(' '.join(content))
    
               

