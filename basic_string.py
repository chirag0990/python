"""
#String is immutable in Python

#All String Methods

# write a string in Python with double quotes
a = "Hello, World!"
print(a)

# write a string in Python with single quotes
b = 'Hello, World!'
print(b)

# write a string in Python with triple double quotes
c = Hello, World!
print(c)

# write a string in Python with triple single quotes
d = '''Hello, World!''' # we can use triple quotes to write a string for multiline commenting
print(d)

# write a string in Python with escape characters
e = "Hello, \"World!\""
print(e)

# write a string in Python with raw string
f = r"Hello, \"World!\""
print(f)

# write a string in Python with unicode
g = u"Hello, \u03A9"
print(g)

# write a string in python with new line
h = "Hello, \nWorld!"
print(h)

# write a string in python 
i = "Hello, 'world!'"
print(i)

#Conceatenation String Operation

# join two strings opertion [Conceatenation String Operation]
string1 = "Hello"
string2 = "World"
string3 = string1 + " " + string2
print(string3)

# join two strings with join method
string4 = "  ".join([string1, string2])
print(string4)

# join two strings with format method
string5 = "{} {}".format(string1, string2)
print(string5)

# join two strings with f-string
string6 = f"{string1} {string2}"
print(string6)  

# Index Method

string7 = "Hello, World!"
print(string7[0]) # print first character

string8 = "Hello, World!"
print(string7[0:12]) # print whole string

string9 = "Hello, World!"
print(string7[6:]) # print from 7th character to end

string10 = "Hello, World!"
print(string7[:12]) # print from 12th character to first character

string11 = "Hello, World!"
print(string11[-13:-1]) # print from 7th character to end

string12 = "Hello, World!"
print(string12[:-2]) # ommit only last two character and print the rest

string13 = "Hello, World!"
print(string13[-2:]) # ommit whole string and left only last two character

string14 = "Hello, World!"
final_string = len(string14) - 1
print(final_string) # print the length of the string

string15 = string14[final_string]
print(string15) # print the last character of the string

string16 = ""
print(string16) # print empty string

string17 = "apple pie"
print(string17[0]+string17[1]+string17[2]+string17[3]+string17[4]+string17[5]+string17[6]+string17[7]+string17[8]) # concatenate the whole string index and print it

string18 = "  "
print(string18) # print empty string with space

string19 = "apple pie"
string20 = "b" + string19[1:]
print(string20) # replace first character with b and print the string

#Exercise
# 1. create a string and print it's length using len() method
string21 = "Hello, World!"
print(len(string21)) 

# 2. create two strings, concatenate them and print the result
string22 = "Hello"
string23 = "world!"
string24 = " ".join([string22, string23])  
print(string24)

# 3. create two strings, use conncatenation to add a space between them and print the result
string25 = "Hello"
string26 = "world!"
string27 = string25 + "  " + string26
print(string27)

string28 = "zinga"
string30 = "".join(["ba",string28]) #join two strings and create a new string
print(string30)

# Manipulation String Operation

string31 = "Hello, World!"
print(string31.lower()) # convert string to lower case

string32 = "Hello, World!"
print(string32.upper()) # convert string to upper case

string33 = "hello, world!"
print(string33.title()) # convert string to title case

string34 = "hello, world!"
print(string34.capitalize()) # convert string to capitalize case

string35 = "hello, world!"
print(string35.swapcase()) # convert string to swap case

string36 = "hello, world!"
print(len(string36)) # check string length

# remove leading and trailing spaces
string37 = "   Hello, World!   "
print(string37.strip()) # remove leading and trailing spaces
print(string37.lstrip()) # remove leading spaces
print(string37.rstrip()) # remove trailing spaces
print(string37.replace(" ", "")) # remove all spaces
print(string37.replace(" ", "_")) # replace all spaces with underscore
print(string37.replace(" ", "-")) # replace all spaces with hyphen
print(string37.replace(" ", ".")) # replace all spaces with dot
print(string37.replace(" ", ",")) # replace all spaces with comma
print(string37.replace(" ", ";")) # replace all spaces with semicolon
print(string37.replace(" ", ":")) # replace all spaces with colon
print(string37.replace(" ", "|")) # replace all spaces with pipe
print(string37.replace(" ", "/")) # replace all spaces with forward slash
print(string37.replace(" ", "\\")) # replace all spaces with backward slash
print(string37.replace(" ", "@")) # replace all spaces with at sign
print(string37.replace(" ", "#")) # replace all spaces with hash
print(string37.replace(" ", "$")) # replace all spaces with dollar sign
print(string37.replace(" ", "%")) # replace all spaces with percent sign
print(string37.replace(" ", "^")) # replace all spaces with caret
print(string37.replace(" ", "&")) # replace all spaces with ampersand
print(string37.replace(" ", "*")) # replace all spaces with asterisk
print(string37.replace(" ", "(")) # replace all spaces with left parenthesis
print(string37.replace(" ", ")")) # replace all spaces with right parenthesis
print(string37.replace(" ", "[[")) # replace all spaces with left square bracket
print(string37.replace(" ", "]]")) # replace all spaces with right square bracket
print(string37.replace(" ", "{")) # replace all spaces with left curly bracket
print(string37.replace(" ", "}")) # replace all spaces with right curly bracket
print(string37.replace(" ", "<")) # replace all spaces with less than sign
print(string37.replace(" ", ">")) # replace all spaces with greater than sign
print(string37.replace(" ", "?")) # replace all spaces with question mark
print(string37.replace(" ", "!")) # replace all spaces with exclamation mark
print(string37.replace(" ", "`")) # replace all spaces with backtick
print(string37.replace(" ", "'")) # replace all spaces with single quote
print(string37.replace(" ", '"')) # replace all spaces with double quote
print(string37.replace(" ", "~")) # replace all spaces with tilde
print(string37.replace(" ", " ")) # replace all spaces with space

# check if string contains only digits
string38 = "1234567890"
print(string38.isdigit()) # check if string contains only digits
print(string38.isnumeric()) # check if string contains only numeric characters
print(string38.isdecimal()) # check if string contains only decimal characters
print(string38.isalnum()) # check if string contains only alphanumeric characters
print(string38.isalpha()) # check if string contains only alphabetic characters
print(string38.islower()) # check if string contains only lowercase characters
print(string38.isupper()) # check if string contains only uppercase characters
print(string38.istitle()) # check if string contains only title case characters
print(string38.isprintable()) # check if string contains only printable characters
print(string38.isspace()) # check if string contains only whitespace characters
print(string38.isidentifier()) # check if string is a valid identifier
print(string38.isascii()) # check if string contains only ASCII characters

#  check starts with end with string

string39 = "Hello, World!"
print(string39.startswith("He"))
print(string39.startswith("he"))
print(string39.endswith("!"))
print(string39.endswith("world!"))

# input string from user

string40 = input("Enter your name: ")
print("Hello, :", string40.capitalize())

# On string Arithmetic Operation

string41 = "41"

print(string41 + string41) # concatenate two strings
print(string41 * 7) # multiply two strings

#Convert String into Numbers

# 1) int = Convert object into integer
# 2) float = Convert object into numbers with decimal point

num = int(input("Enter a number: "))*3
print(num) # print the number

num = float(input("Enter a number: "))*3
print(num) # print the number

string42 = 10

print("I'm eating" + str(string42) + " apples") # convert integer to string and concatenate with string

string43 = 10
string44 = 20
print("Only" + str(string43 - string44) + "apples") # convert integer to string and concatenate with string

string45 = 10
strings46 = 20
day = "Today"
print(day + " I have ate" +  " "+ str(string45) + " apples and" +  " " + str(strings46) + " oranges") # convert integer to string and concatenate with string

# {} curly braces use for formatting no nedd to convert to string
string47 = 10
string48 = 20
day = "Today"

print(f"{day} I have ate {string47} apples and {string48} oranges") # convert integer to string and concatenate with string

"""
"""
### Exercise #####

weight = 0.2
animal = "newt"

print(str(weight) + " kg is the weight of the" + " " +str(animal) + ".")
print("{} kg is the weight of the {}.".format(weight, animal))
print(f"{weight} kg is the weight of the {animal}.")"""

"""
# Find() Method : find the location of one string within another string (a substring)

string49 = "Hey string I found you"
print(string49.find("string")) # find the location of string in string49

print(string49.find("String")) # I am getting -1 because the string is not found in string49

#string50 = "Hey string I found you 555555"
#print(string49.find(5)) # I am getting error because the find() method only accepts string as an argument

string51 = "Hey string I found you 555555"
print(string51.find("555555")) # find the location of 555555 in string51

# replace() Method : replace a substring with another string

string52 = "Hey string I found you"
print(string52.replace("string", "new string")) # replace string with new string

###Exercise #####

string53 = "a"
print(string53.replace("a", "AAA")) # replace a with AAA

string54 = "Somebody said something to Samantha"
print(string54.replace("s", "x")) # replace Somebody with Somebody else

"""

# 3S' F-String 
"""
We will get a review of the two old school string formatting methods:
1). % string formatting
2). str.format() method
"""
"""
# 1) % string formatting 
f_name = "chirag"
m_name = "baldevbhai"
l_name = "patel"
age = 28
profession = "Artificial Intelligence Engineer"

print("Hello, my name is %s %s %s. I am %s years old and I am a %s." % (f_name, m_name, l_name, age, profession)) # using % operator

# 2) str.format() method

f_name = "chirag"
m_name = "baldevbhai"
l_name = "patel"
age = 28
profession = "Artificial Intelligence Engineer"

print("Hello, my name is {} {} {}. I am {} years old and I am a {}.".format(f_name, m_name, l_name, age, profession)) # using str.format() method


person = {"f_name":"chirag", "m_name":"baldevbhai", "l_name":"patel", "age":28, "profession":"Artificial Intelligence Engineer"}

print("Hello, my name is {f_name} {m_name} {l_name}.".format(f_name = person['f_name'], m_name = person['m_name'], l_name = person['l_name'])) # using str.format() method

print("Hello, my name is {0} {1} {2}. I am {3} years old and I am a {4}.".format(f_name, m_name, l_name, age, profession)) # using str.format() method

print("Hello, my name is {f_name} {m_name} {l_name}. I am {age} years old and I am a {profession}.".format(**person))
"""
# New way of formatting strings in Python 3.6 and above
f_name = "chirag"
m_name = "baldevbhai"
l_name = "patel"
age = 28
profession = "Artificial Intelligence Engineer"

print(f"Hello, my name is {f_name} {m_name} {l_name}. I am {age} years old and I am a {profession}.") # using f-string
print(F"Hello, my name is {f_name} {m_name} {l_name}. I am {age} years old and I am a {profession}.") # using f-string



######### String Exercise ##########

# 1) Double Quotation marks inside the string

string1 = 'fashion "is" a way of life.' 
print(string1)

#2) An apostrophe inside the string
string2 = "fashion's a way of the life"

#3)Multiline with white space preserved (use """ """")
string3 = """ hey man good morning. what do you do.
have any proble few hours back. because you'r fighting with someone."""
"""
print(string3)

#4) Multiline with white space not preserved ( use "" and \)
string4 = "hey man good morning. what do you do. \
have any proble few hours back. because you'r fighting with someone."
print(string4)


#### Exercise2 #####

# 1) conceatenate two strings without space and  with space

string5 = "Hello"
string6 = "brother!"
string7 = "How'r You?, Good Morning!"

print(string5 + string6 + string7)
print(string5 + " " + string6 + " " + string7)

##### Exercise3 #####

# 1) print the string "zing" by using slice notation to specify the correct range of characters in the string "bazinga".

string8 = "bazinga"
print(string8[0:])
print(string8[2:])
print(string8[2:-1])
print(string8[2:6])

##### Exercise4 #####

# 1) four strings wa want to just apply lowercase and upper case method on strings

string1 = "Animals"
string2 = "Badger"
string3 = "Honey Bee"
string4 = "Honey Badger"

print(string1.lower())
print(string2.lower())
print(string3.lower())
print(string4.lower())

print(string1.upper())
print(string2.upper())          
print(string3.upper())
print(string4.upper())

### Exercise5 #####

# Remove white space from the string

string1 =  "    Filet Mignon"
string2 = "    Filet Mignon   "
string3 = "Filet Mignon    "

print(string1.lstrip())
print(string2.strip())
print(string3.rstrip())

#### Exercise6 #####

# check the string begining of the letters or strings

string1 = "Becomes" 
string2 = "becomes"
string3 = "Bears"
string4 = " beAlerts"

print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))


# we want to do all strings getting True 

print(string1.lower().startswith("be"))
print(string2.startswith("be"))
print(string3.lower().startswith("be"))
print(string4.lstrip().startswith("be"))

##### Exercise7 #####

# interact with user input 

# collect the user input
string1 = input("Enter a string: ")

#convert the string to lower case and given the length of the string 
print(string1.lower())

#display the length of the string
print(len(string1))
"""
##### Exercise8 #####

"""write a program that you’re going to name first_letter.py,
 and it should prompt the user for an input, 
 giving you the prompt string "Tell me your password:"
 and then the program should determine the first letter of the user’s input, 
convert that letter to uppercase, and display it back."""
"""user_input = input("Tell me your password: ")
print(user_input[0].upper())

string1 = int(input("Enter your number: "))
string2 = int(input("Enter your number: "))
string3 = float(string1) * float(string2)
print(f" The product of {string1} and {string2} is muliply by {string3} .")
"""
"""
####### Exercise9 #####

weight = 0.2
animal = "newt"


print("{} kg is the weight of the {}.".format(weight, animal))

print(f"{weight} kg is the weight of the {animal}.")

"""

# Correct answer:
vulcan_logic = 'Spock said, "Live long and prosper."'

# You could also write the string like this:
vulcan_logic = "Spock said, \"Live long and prosper.\""

######## Exercise10 #####

a = "AAA"
print(a.find("a"))
print(a.find("AA"))
print("BAA".find("A"))

######### Exercise11 #####
a = "Somebody said something to Samantha." 
print(a.replace("s","x"))

a = input("Enter the string: ")
b = input("Enter the find string: ")
print(a.find(b))

#### Challenging Exercise #####

a = "Leet Hacker"
print(a.replace("e", "3").replace("a","4"))

a = input("Enter the user input: ")
a = a.replace("e","3") \
      .replace("a","4")
print(a)
