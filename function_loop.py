# cretae a function 

def shout_and_loud(input_string):
    """ This functions works with print and return the string in uppercase""" # docstring
    data_string = input_string.upper()
    print(data_string)
    return data_string

shout_and_loud("hello world")
data2 = shout_and_loud("hello world")
#print(help(shout_and_loud))

# create a function that takes a color and returns a string with the color
def color_choice(color):
    """ This function takes a color and returns a string with the color"""
    if color == "red":
        print(color.upper())
        return color
    elif color == "blue":
        print(color.lower())
        return color
    else:
        return None
    
color_data = color_choice(input("Enter a color: "))

#   Whil loop & for loop
#print 1 to 10 numbers using while loop
n=1 
while n <= 10:
    print(n)
    n = n +1

# print 1 to 5 using while loop
n = 1
while n <= 5:
    print(n)
    n += 1

# print 1 to 5 using for loop
for i in range(1,6):
    print(i)

num = float(input("Enter a positive number: "))

while num <= 0:
    print("Please enter a positive number.")
    num = float(input("Enter a positive number: "))
    
for i in range(1,4):
    for j in range(1,4):
        print(f"i:{i}, j:{j}")

        
        
    