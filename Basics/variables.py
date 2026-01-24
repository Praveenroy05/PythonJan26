# Variables - Storage - Which stores either a single value or multiple values

# Syntax:
# variableName = value

print('Welcome to Python')

age = 35  # Global variable
Age = "Test"

# type(variable) - It will return the data type of a variable

print(type(Age))

# System.out.println()
# console.log()
# print(....)

# age: 35
# Age : Test

'''
# Combine or Merge 2 or more variables/values - we have 2 ways
1. Using + operator - Will work only if you have both the variable/value are of same data type
2. Using ,(comma)

'''

print("age: ", age)
print("Age: " + Age)

# Scope of a variable"

'''
 Scope - There are 2 types of scope
 1. local - Any variables that you define inside a function is known as local variable
 2. global - Outside of the function - global scoped variable
'''
#
# if(true) {
#     #xyz
# }
#     else{
#
# }
'''
if 2>1:
    print("2>1")
    print("if")
else:
    print("2<1")
'''


def sum():
    x = 10  # local scoped variable
    y = 20
    print(x + y)
    print(age)


sum()
# print(x)

a = 10  # global scoped variable


def sum1():
    x = 10  # local scoped variable
    y = 20
    print(x + y)
    #   globals(a) = 50
    print(a)


sum1()

# Assignment - try to declare a variable and multiple variable in the print() and print it on the console

# Data Types and Operators
