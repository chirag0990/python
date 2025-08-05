# Numeric tyes in python 

# int = postive or negative whole numbers

# float = positive or negative numbers with decimal points

# complex = complex numbers with real and imaginary parts (3 + 4j)


a = 5

print(a)

print(type(a)) # type() function returns the type of the object

# binary = 0b1010 # binary numbers start with 0b

# octal = 0o10 # octal numbers start with 0o

# hexadecimal = 0x10 # hexadecimal numbers start with 0x

######### Arithmetic Operators #########

a = 5
b = 2 

print(a + b) # addition
print(a - b) # subtraction
print(a * b) # multiplication
print(a / b) # division
print(a // b) # floor division
print(a % b) # modulus
print(a ** b) # exponentiation

#####Uniary Operators #####
a = 5
print(-a) # negation
print(+a) # positive
print(abs(a)) # absolute value
print(pow(a, 2)) # power
print(round(a)) # round to nearest integer
print(round(2.5, 1)) # round to 1 decimal place

print(float.is_integer(2.5)) # check if float is integer
print(float.as_integer_ratio(2.0)) # check if float is integer
######### highest to lowest Operators #########

# 1. Exponentiation (**)
# 2. Unary plus and minus (+a, -a)
# 3. Multiplication, Division, Floor Division, Modulus (*, /, //, %)
# 4. Addition and Subtraction (+, -)
# 5. Bitwise Shift Operators (<<, >>)
# 6. Bitwise AND (&)
# 7. Bitwise XOR (^)
# 8. Bitwise OR (|)
# 9. Comparison Operators (==, !=, <, >, <=, >=)
# 10. Identity Operators (is, is not)
# 11. Membership Operators (in, not in)
# 12. Logical Operators (and, or, not)
# 13. Assignment Operators (=, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, >>=, <<=)
# 14. Conditional Expressions (if-else)
# 15. Lambda Expressions (lambda)
# 16. Comma Operator (,)


print(round(2.3))
print(round(2.3, 1))
print(round(2.345, 2))
print(round(2.3467, 3))
print(round(2.6))
print(round(2.5, 1))
print(round(2.555, 2))

print(abs(-5)) # absolute value
print(abs(5)) # absolute value
print(abs(-5.5)) # absolute value
print(abs(5.5)) # absolute value
print(abs(-5.5 + 2j)) # absolute value
print(abs(5.5 + 2j)) # absolute value
print(abs(-5 + 2j)) # absolute value
print(abs(5 + 2j)) # absolute value
print(abs(-5 - 2j)) # absolute value
print(abs(5 - 2j)) # absolute value
print(abs(-5 + 2j)) # absolute value
print(abs(5 + 2j)) # absolute value
print(abs(-5 - 2j)) # absolute value

print(pow(2, 3)) # power
print(pow(2, 3, 5)) # power with modulus
print(pow(2, 0.2)) # power with modulus
print(pow(2, -3)) # power with modulus
print(pow(2, -0.5))


print(0b1010)
print((10).bit_length())# bit length
print((10).bit_count()) # bit count

# The round() function rounds a number to the nearest integer or to a specified number of decimal places.
# The abs() function returns an absolute value of a number or the magnitude of a complex number. 
"""The pow() function performs largely the same mathematical operation as the ** operator in Python, 
but it also provides a shorthand notation for calculating the modulo of the resulting power."""

###### Formatting Numbers as Strings ######
price = 3.9
print("The price is ${price:.2f}") # format float to 2 decimal places
print("The price is ${price:15.2f}")
print("The price is ${price:<15.2f}")
print("The price is ${price:^15.2f}")
print("The price is ${price:015.2f}")
print("The price is ${price:<015.2f}")
print("The price is ${price:,.2f}")


######## Complex Numbers ########
a = 3 + 4j
b = 2 + 3j
c = a + b
print(c.real)
print(c.imag)
print(c.conjugate())

############# Exercises #############

num1 = 25000000
num2 = 25_00_00_000
print(num1)
print(num2)

"""Write a program that assigans the floating-point literal 175000.0 to 
the variable num using E notation and the prints 
num in the interactive window."""  

num = 175e3
print(num)
num1 = 175e-3
print(num1)

""" write a program try to find the smallest exponent N for which 2e<N>,
 where N is relpace with you numbers, and returns inf."""

print(float('inf')) # infinity
print(float('nan')) # not a number
print(float('inf') - float('inf')) # not a number
print(float('inf') + float('inf')) # infinity
print(float(2e500))
import sys 
print(sys.float_info)

""" Print the result of the calculation 3 ** .125 as a fixed-point number with 3 decimal places."""

print(3 ** .125)

from decimal import *
getcontext().prec = 1000
print(Decimal(3) ** Decimal(".125"))
print(Decimal(3) ** Decimal(.125))


""" Print the number '150000' as a currency with the thusands group with a comma 
 Currency should be displayed with a two decimal places."""

print(format(150000, '.2f'))
print(format(150000, ',.2f'))
print(f'${150000:,.2f}')

""" Print the result of 2/10 as a percentage with no decimal places. """

a = 2
b = 10
print(f'{a/b:.0%}')


""" Write a program called that recieved two numbers
 from the user and displays the first number raised to the power of the second number """

a = int(input("Enter the first number: "))
b = int(input("Enter the second number:"))
print(f'{a} raised to the power of the {b} is {a ** b}')
print(f'{a} raised to the power of the {b} is {pow(a, b)}')
print(f'{a} raised to the power of the {b} is {a ** b:.2f}')
print(f'{a} raised to the power of the {b} is {pow(a, b):.2f}')

""" write a program that asks the user to input a number  and the displays that number rounded to two decimal places.
when run, your program should look like this:
* enter the number: 5.432
* 5.432 rounded to 2 decimal places is 5.43"""

a = float(input("Enter the number: "))
print(f'{a} rounded to 2 decimal places is {round(a, 2)}')
print(f'{a} rounded to 2 decimal places is {format(a, ".2f")}')
print(f'{a} rounded to 2 decimal places is {f"{a:.2f}"}')

""" write a program that asks the user to input a number  and the displays that absulate value of that number.
when run, your program should look like this:
* enter the number: -10
* The absolute value of -10 is 10.0"""

a = float(input("Enter the number: "))
print(f'The absolute value of {a} is {abs(a)}')

""" Write a program that asks the user to input two numbers by using input() twice,
then displays whether the difference betweem those two numbers is an integer."""

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

diff = a - b

print(f'the differnece between {a} and {b} is an inetger ?{diff.is_integer()}! ')


