# Operator - It is a special symbol which perform some kind of operations

'''
  There are different types of operators:

  1. Arithmetic Operators
  2. Comparison Operators
  3. Logical Operators
  4. Assignment Operators



  1. Arithmetic Operators - An Operator which will perform mathematical Operations

       1. Addition (+)
       2. Subtraction (-)
       3. Multiplication (*)
       4. Division (/) - 9/2 - 4.5
       5. Modulus (%) - Remainder after the division - 9%2 - 1
       6. Exponential (**) - Power of a number - 5 **5 5^5 - 5*5*5*5*5
       7. Floor Division (//) - Integer par of division result - 9/2 - 4


  2. Comparison Operators - Compares the two values and returns the result in the form of boolean

      1. Equal to (==) - Compares whether the values are same or not
      2. Not Equal to (!=) -
      3. Greater than (>)
      4. Greater than or equal (>=)
      5. Less than (<)
      6. Less than or equal (<=)

  3. Logical Operator - Logical operators validates 2 different conditions or expression

      1. and - Both of the condition has to be true to get the result as true
      2. or - Either of the condition has to be true to get the result as true
      3. not - Reverse the result from true to false and vice-versa

      (10>5) - (6>1)

      True and True   - True
      True and False  - False
      False and True  - False
      False and False - False



      True or True   - True
      True or False  - True
      False or True  - True
      False or False - False


      not(True) - False
      not(False) - True

  4. Assignment Operator (=) - Assign the value to a variable

  a = 30



'''


a = 24
b = 5

print("Addition", a+b)
print("Subtraction", a-b)
print("Multiplication", a*b)
print("Divison", a/b)
print("Modulus", a%b)
print("Exponential", 5 ** 3) # 5^2 - 5*5*5
print("Floor Division", a//b) # 4.8


print("*********Conditional Operators")
a1= 20
a2= "20"
print(a1 == a2)

print(a1 != a2)

print(a1 > a2)
print(a1 >= a2)
print(a1 < a2)
print(a1 <= a2)

print("*********Logical Operators")


marks = 85

print((marks > 80) and (marks < 89)) # True and True - True
print((marks > 80) and (marks > 85)) # True and False
print((marks < 80) and (marks > 80)) # False and True
print((marks < 80) and (marks > 90)) # False and False


print((marks > 80) or (marks < 89)) # True and True - True
print((marks > 80) or (marks > 85)) # True and False
print((marks < 80) or (marks > 80)) # False and True
print((marks < 80) or (marks > 90)) # False and False


#>90 - A
#>80 -89 - B

print(not(marks > 80))
print(not(marks > 90))









