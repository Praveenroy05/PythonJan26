# Function - It is a block of code that performs a specific.

'''

1. Help us in terms of minimizing the duplication
2. Reducing the maintenance of the code
3. Introduces a concept of reusability



1. fill the username
2. fill the password
3. click on login button


100 Tcs - 300 lines of code - login
100 steps that for maintenance - password


def login():
    fill the username
    fill the password
    click on login button

login() - 100 tcs  - 104 lines - saved 196 lines of code
1 step in maintenance - saved 99 steps
reusability


Syntax:

def functionName(parameter):
    code
    return ....

def - keyword which means define something
functionName - Function Name
(parameter) - Accepts input value
: - Function body starts from : -  {}

Note: TO use the function anywhere we need to call the defined function -
Call the function by using the name of the function followed by ()

return - the function will return some value when you call the function


'''

# Function with no arguments and non-returning


def welcome():
    print("Welcome to AI LLM course")


welcome()

# non-parameterised and returning function


def greet():
    return "Python is a simple language"


result = greet()
print(result)


# Parameterised function and non-returning


def print_value(param):  # param - parameter
    print(param)


print_value("Login")   # Login - Argument


# parameterise and returning function

# expected status = 200
# actual status  = 200


def check_status(expected, actual):
    return expected == actual


status_result = check_status(200, 200)
print(status_result)
status_result1 = check_status(200, 400)
print(status_result1)


def add(a,b):
    print(a+b)


add(5,5)


def add(a,b,c):
    print(a+b+c)


add(3,5,20)

# Defining a function with the same name but having different parameter is know as Method Overloading

# variable argument - *args


# Non-primitive - list, tuple, dictionary, set

def display(*a):
    print(a)


display(1)
display(1,2,3,4,5,7,7,8,8,"TS", 28734689348)













