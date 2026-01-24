'''

Conditional Statements:

   It performs different actions depending on the result.

   Allows us to execute different block of code for different condition


   1. if statement - It validate the positive condition
   2. if else statement
   3. if elif else statement
   4. Nested if statement
   5. match-case statement


   1. if statement : This will validate a positive scenario for the condition
   Syntax:
   if condition:
       code


   2. if else statement : This will validate positive scenario and negative scenario
   Syntax:
   if condition:
       code
   else:
       code

   3. if elif else statement - This statement validates mutliple condition.
   Depending on the condition result it executes specific block of code.

   Syntax:

   if condition1:
       code - This will get executed when condition 1 is True
   elif condition2:
       code - This will get executed when condition 2 is True
   elif condition3:
       code - This will get executed when condition 3 is True
   else :
       code - This will get executed when all the condition are False


   4. match case statement (switch statement) - It also validates multiple condition.
   Match case will directly jump to the block where the condition is matching
   not like if elif which validate all the different condition.

   Syntax:
    match expression:
        case "expectedValue":
            code
        case "expectedvalue1":
            code
        case _:
           code

'''

if 100 > 20:
    print("100>20")

print("If statement completed")

age = 10

if age >= 18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")



# if elif else statement

broswer = "edge"

if broswer == "chrome": # "firefox" == "chrome"
    print("Launch the chrome browser")
elif broswer == "firefox":
    print("Launch the firefox browser")
elif broswer == "safari":
    print("Launch the safari browser")
else:
    print("Invalid browser")


browserName = "safari"
match browserName:
    case "chrome":
        print("Launch the chrome browser - match case")
    case "firefox":
        print("Launch the firefox browser - match case")
    case "safari":
        print("Launch the safari browser - match case")
    case _:
        print("Invalid browser")


# Write a program to define the grading system:
# Marks > 90 - A
# Marks > 80 -90 - B
# Marks > 70-80 - C
# Marks < 70 - D





