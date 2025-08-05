# Exercise 1 : Greet Someone
def greet(name):
    """This function greets called the name passed as an argument."""
    person = f"Hello, {name}!"
    print(person)
    return person
# Call the function with a name
greet("Chirag")

# Exercise 2: Calculate cube of a number
"""def cube(num):
    This function calculates the cube of a number.
    result = num ** 3
    print(result)
    return result
# Call the function with a number
cube(3)"""

#def cube(num):
"""This function calculate the cube of number."""
#    return pow(num, 3)

# call the function with a number
# print(cube(1))
# print(cube(2))
# print(cube(3))

# Exercise 3: temperature conversion

# def convert_cel_to_far():
"""This function converts Celsius to Fahrenheit."""
    # celsius = float(input("Enter temperature in Celsius: "))
    # fahrenheit = (celsius * 9/5) + 32
    # print(f"{celsius}°C is equal to {fahrenheit}°F")
    # return fahrenheit
# Call the function to convert temperature
# convert_cel_to_far()

# def convert_far_to_cal():
"""This function converts fahrenheit to Celsius."""
    # fahrenheit = float(input("Enter Temperature in Fahrenheit: "))
    # celsius = (fahrenheit - 32) * 5/9
    # print(f"{fahrenheit}°F is equal to {celsius}°C")
# Call the function to convert temperature
# convert_far_to_cal()

# prompt the user: to enter the temperature
# 1. Fahrenheit -> display the Celsius
# 2. Celsius -> display the Fahrenheit
# 3. Display all convertered temperatures rounded to 2 decimal places

# temp_far = 72 #T: Prompt User
# temp_cel = convert_cel_to_far()
# print(f"{temp_far:.2f}")

# temp_cel = 22 #T: Prompt User
# temp_far = convert_cel_to_far()
# print(f"{temp_cel:.2f}")

# #Exercise 4: using for loop print the numbers from 1 to 10
# for i in range(10):
#     print(i)
# for i in range(2,10):
#     print(i)
# for i in range(1, 11):
#     print(i+1)

# exercise : print the duble the numbers 
def dubble_numbers(number):
    return number * 2

# call the function with a number
numbers = 2
for _ in range(3):
    numbers = dubble_numbers(numbers)
    print(numbers)

    

############# Task : Track Your Investments #############

## That tracks the growing amount of an investment over time.
## The initial deposit for an investment is called the principal amount. 
## Each year, the amount increases by a fixed percentage, called the annual rate of return.

#def invest(amount, rate, years):

# The function should then print out the amount of the investment, rounded to two 
# decimal places, at the end of the each year for the specified number of years.


def invest(amount, rate, years):
    """This function calculate the invesyment amount over the years."""
    for years in range(1, years + 1):
        amount += amount * (rate /100)
        print(f"year {years}: ${amount:.2f}")
    return amount
# Call the function with an amount, rate, and years
amo = float(input("Enter the inital investment amount: "))
rat = float(input("Enter the annual rate of return (in %): ")) 
yrs = int(input("Enter the number of years to invest: "))
invest(amo, rat, yrs)

