# Exercise 1: String Literals
# Double qutations marks inside the string
a = 'hi, "/hello world/"'
print(a)
#An apostrophe inside the string
b = "hi, how's it goint?"
print(b)
#Multiple lines with preserrving white space
c = """ this is a string,                    
 
  
   
    with multiple lines and preserving white space"""
print(c)
#coded on multiple lines but printed on a single line
d = """ this is a string, \
with multiple lines \
but printed on a single line"""
print(d)

#Exercise 2: String Concatenation

# create a two string and concenate them also # add a space between them

first_name = "Chirag"
middle_name = "Baldevbhai"
last_name = "Patel"

print(first_name + " "+ middle_name + " " + last_name)

a = "bazinga"
print(a[2:6])
print(a[2:6:1])  # slicing with step
print(a[-5:-1])

# Exercise 3: String upper and lower case

a = "Animals"
b = "Badger"
c = "Honey  Bee" 
d = "Honey Badger"
print(a.lower())
print(b.lower())
print(c.lower())
print(d.lower())
print(a.upper())
print(b.upper())
print(c.upper())
print(d.upper())

#Exercise 4: String Space removal
a = "    Filet Mignon"
b = "Brisket    "
c = "   Cheeseburger   "
print(a.lstrip())
print(b.rstrip())
print(c.strip())

#Exercise 5: String startswith

a = "Becomes"
b = "becomes"
c = "BEAR"
d = "  bEautiful"

print(a.startswith("be"))
print(b.startswith("be"))
print(c.startswith("be"))
print(d.startswith("be"))

print(a.lower().startswith("be"))
print(b.startswith("be"))
print(c.lower().startswith("be"))
print(d.lower().lstrip().startswith("be"))

#Exercise 6: create a user input

# 1 create a user input

user_input = input("Enter a string:")
print(user_input.lower())
print(len(user_input))

#Exercise 7: Pick Apart your user input

a = input("Tell me your password:")
print("The first letter you entered was:",a[0].upper())

#Exercise 8: working with strings and numbers

a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))

c = float(a * b)

print(f"The product of {a} and {b} is {c}.")

#Exercise 9: Streamline your point
weight = 0.2
animal = "newt"
# using format method
print("{weight} kg is the weight of the {animal}.".format(weight=weight, animal=animal))
#using f-string
print(f"{weight} kg is the weight of the {animal}.")

# exersie 10: find a substring
print("AAA".find("a"))
print("AAA".find("A"))
print("BAA".find("A"))
print("AAAS".find("AS"))

#Exercise 11: String replace
a = "Somebody said something to Samantha"
print(a.replace("S","X"))
# first replace all 'e' with '3' and then replace all 'a' with '4'
a = input("Enter a substring: ")
a = a.replace("e", "3")
a = a.replace("a", "4")
print(a)

# Second maethod used

a = a.replace("e", "3")\
    .replace("a", "4")
print(a)
