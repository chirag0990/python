##############  ARGUMENT PARSER ##############

# it's a powerful library for managing command-line arguments

# There are five basic steps:

# 1. Import the argparse module
# 2. Create a parser object
# 3. Add one or more arguments to the parser
# 4. Call .parse_args() Parse the arguments
# 5. Acts on the results

# Example 1

#import sys

#name = sys.argv[1]
#num = int(sys.argv[2])

#for _ in range(num):
#    print(f"I'm sorry {name}, I can't do that.")

# Example 2 using argparse

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name", help="The name of the person to apologize to")
parser.add_argument('num', type=int, help="The number of times to apologize")
args = parser.parse_args()
for _ in range(args.num):
    print(f"I'm sorry {args.name}, I can't do that.")


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

######### Positional vs Optional Arguments #########

# Positional arguments are required and must be provided in the order they are defined.
# Optional arguments are not required and can be provided in any order. indicated by flags.
# Optional arguments are usually used to modify the behavior of the script or provide additional information.
# They can be specified with a single dash (-) or double dash (--), followed by the argument name.  


############### Actions ###############

# The action parameter to .add_argument() allows you to change what happens when an the arguments processed.

########## Comman action are ##########

# - store: Store the value of the argument (default) or keep the parameter in the namespace, this is the default action.
# - store_const: Store a constant value when the argument is provided.
# - store_true: Boolean flag, True if the option is given.
#  - store_false: Boolean flag, False if the option is given.
# - append: Store as a list, option can be given multiple times.
# - help: invoke help text and exit, to replace "-h" 
# - version: show the version of the program and exit.
# - count: store a counter equal to the number of times an option has been given
  

# store_const : Store a constant value when the flag is present.
# append_const : Store a list containing a constant value for each time the falg is given.
# extend : Store a list contatining each parameter given for the flag; support multiple parameters.

################ Hnadling Multiple Arguments ################

# The nargs parameter to .add_argument() allows you to change how many things are consumed 
# For postional arguments it consumes this many arguments
# For optional arguments it consumes this many parameters after the flag

# Note : refer code file harry.py

## Acceptable nagrs values are:

# 1) A number
# 2) "*" : 0 or more arguments (default for positional arguments)
# 3) "?" : 0 or 1 arguments
# 4) "+" : 1 or more arguments
# 5) args.REMAINDER : zero or more arguments, all remaining arguments after the flag.

############### Less Common Features ################

##### MISCELLANEOUS ###########

# Other things you can do with the parser:

# 1) Restrict valid parameters to a list of known values
# 2) Make flags mutually exclusive 
# 3) Read arguments from the files

# optional flags have optional but required flags have mandatory 

# example of code file is forest.py

# .add_mutually_exclusive_group() method, you get a group object, which you can configure.

# example code. starwars.py

######### Parameters to argument parser ##############

# 1) allow_abbrev is a parameter if we passed false then disallowed option flags.

# 2) fromfile_prefix_chars is a parameter allows for given an arguments that starts with the @ character in this case and contains the name of a file.

# 3) add_help=False : to turn off the "-h" features

# 4) prefix_chars="/" : change the prefix character for a flag to a different value.

############# Callable Types, Custom Actions #################

################ Types #################

# Setting an argument's "type" allows you to convert the given value to that type

# Common uses are int and float

# The type parameter supports any callable, passing the given value in posiiblies:

# ord: get the code-point value of a character passed in 
# open: open the given file name 
# pathlib.Path: convert the string to a "Path" object

############# Types ###############

#Be careful: just because you can doesn't mean you should

# bool: won't work as expected, empty strings are False, all non-empty strings are True

# Using decoders for JSON or YAML, or the FileType object can get messy

 # 1) Error reporting will be generic
 # 2) Example : a badly formed JSON  file will report as if you gave an incorrect argument 

# Better off not getting too fancy

########### Custom Action ###########

# Write your own action for storage
# Inherit from argparser.Action

# for example above concept yoda.py file 

############## SUB PARSER ##########

# A sub-parser allows you to write command to your script
# for example: git checkout, git status
# Use the .set_defaults()method to attach a function

# python code indy.py
                


