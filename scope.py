########## SCOPE ##########
"""
For example, anytime you assign a variable, you create a name. 
Python uses the location of the name assignment to associate it with a particular scope. 
That scope determines where you can use that variable within your program."""
# In Python, scope refers to the region of a program where a variable is accessible.


# we have four scopes:
# 1. local scope: variables defined within a function
# 2. enclose scope: variables defined in the nearest nonlocal scope that is not global
# 3. global scope: variables defined at the top level of a module or script
# 4. built-in scope: variables defined in the built-in namespace

# Local Scope
def local_scope():
    total = 0  #local variable
    print(f"Local Scope: {total}")
    return total
local_scope()

# we can access the local variable from the enclosing scope
def local_scope():
    def enclose_scope():
        print(f"Enclose Scope: {total}")  # this will raise an error because total is not defined in this scope
    total = 10  # local variable
    enclose_scope()
    print(f"Local Scope: {total}")
local_scope()

# First we define a global variable
# Now we can access the global variable from the local scope
# Global Scope
def local_scope():
    def enclose_scope():
        print(f"Enclose Scope: {total}")
    
    enclose_scope()
    print(f"local Scope: {total}")

total = 10  # global variable
local_scope()

# Example : 2 
def local_scope():
    def  enclose_scope():
        total = 5  # local variable
        print(f"Enclose Scope: {total}")
        
    enclose_scope()
    total = 10 #local variable
    print(f"Local Scope: {total}")

total = 20  # global variable
print(f"Global Scope: {total}")
local_scope()


# Example : 3
def local_scope():
    def enclose_scope():
        nonlocal total  # this will refer to the nearest enclosing scope variable
        total = 5  # this will modify the enclosing scope variable
        print(f"Enclose Scope: {total}")

    total = 10  # local variable
    enclose_scope()
    print(f"Local Scope: {total}")
total = 20  # global variable
print(f"Global Scope: {total}")
local_scope()       

# Exploring the Global Statements
# The global statement allows you to modify a global variable from within a function

#counter = 0 # global variable

#def increment_counter():
#    counter = counter + 1 # incrementing the global variable

#increment_counter() #UnboundLocalError: local variable 'counter' referenced before assignment

# how to fix the above error

# Example : 1
counter = 0  # global variable
def increment_counter():
    global counter  # declare counter as global
    counter += 1  # incrementing the global variable
    print(f"Counter: {counter}")

increment_counter()  # Counter: counter = 1

# Example : 2

counter = 0  # global variable
def increment_counter():
    global counter  # declare counter as global
    counter += 1  # incrementing the global variable
  

increment_counter()  # Counter: counter = 1
print(f"Counter: {counter}") # we did not get error because we declared counter as global variable

# Note: 

""" but it's bad practise to use global variables in this way 
 if we have big code base, it will be hard to track the changes in the global variable
 so we should avoid using global variables in this way """

### Good Programming Practice ###

# 1). Use local names rather than global names
# 2). Write self-contained functions that do not rely on global variables
# 3). Try to use unique object names, no matter what scope they are in
# 4). Avoid global name modifications throug out your code

# for example : 1

counter = 0 

def updated_counter(current_counter):
    return current_counter + 1

counter = updated_counter(counter)  # this will return 1
print(f"Counter : {counter}")  # Counter: 1

# for example using local scope


counter = 0 

def updated_counter():
    counter = 0 
    counter =  counter + 1
    print(f"Counter : {counter}")  # Counter: 1
    return counter

updated_counter()
