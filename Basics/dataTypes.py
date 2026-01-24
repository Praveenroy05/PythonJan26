# Data type - A type of data that a variable is storing

# 2 Types of data types:

a = 10

'''
1. Primitive data type - Which stores a single value
a = 10

   1. int
   2. float
   3. string
   4. boolean 
   
2. Non-primitive data type - Which stores more than 1 value
  
   1. list - []
   2. tuple - ()
   3. Dictionary - {}
   4. set - {} - unique - {1,2,3,4,1,2,3,4}
   
   
   
   
   # 1. int - An integer is a whole number without decimal.
      1. Positive - 90, 80
      2. Negative - -45, -20
      3. Zero - 0
      
   
   # 2. float - A number along with the decimal 
   
   marks = 87.5
   percentage = 67.09
   
   # 3. string - sequence of characters or combination of characters
   
   There are 3 ways in which we can defines string in Python
   
   1. By using single quote
   2. By using double quote
   3. By using 3 times single quote or """
   
   
   # 4. Boolean - Boolean has only 2 values
     1. True
     2. False
      
      
   
   
'''

users = 50
score = 100
temperature = 0.6

# type() - Which will return the data type of a variable

print(type(users))
print(type(temperature))

print(users)
print(temperature)

str = 'This is a single quote string'
str1 = "This is a double quote string"

# whenever you want to declare a string in a multi-line there we can use ''' or """

str2 = """ This is 
a multi line
string """

print(str2)

char = '10'
print(type(char))

expected = 200
actual = 201

isAdmin = False
isEmployee = True

print(expected == actual)

# True and true , False and false are not same
print(5 > 2)

if 5 > 20:
    print("5>2")


'''
Create variable :

Model name - ChatGpt
Score - 80
Test Passed = true


print the variable along with the types

'''