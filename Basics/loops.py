'''

Loops - Execute same block of code multiple times


1. for loop - Execute a sequence of statements multiple time depending on the condition
2. while loop - Execute a sequence of statements multiple time depending on the condition till the condition is True
as soon as the condition becomes false the loop will be terminated.


When do we for and while loop

1. If you know how many times you have to execute the iteration - for loop
2. If you do not know how many time we have to execute the iteration - while loop

1. for loop:
syntax:

for variable in sequence(list, dictionary, string..., range):
    statement(s)


2. while loop: Is a condition based loop

Syntax:

initialise the variable
while condition :
    code
    increase/decrease the value by 1





'''

print(1)
print(2)
print(3)
print(4)
print(5)

for i in range(1, 50, 3):
    print(i)
'''
range(startIndex, endIndex, step)

startIndex(Optional) - Starting value of the range - By default it will have a value as 0
endIndex - last value of the range
step(Optional) - By default the step is 1
    
'''

list = [10,20,30,40,"JS", "TS", "Python"]

for element in list:
    print(element)


# Assignment:

str = '''This is a python string
    write a program to print only the vowel(a,e,i,o,u) part
    of the string'''

  # if char in 'aeiou'


# while loop -
# function -
# non-primitives

# reading data from a file
# Exception handling


# print 1 to 5

# i = 1
# while i < 6:   # 2 < 6
#     i = i + 1
#     if i == 3:
#         continue # 3
#     print(i)


i = 1
while i < 6:
    i = i+1
    if i == 3:
        continue
    print(i)
    # i +=1 = i = i+1

attempt = 0

while attempt <= 3:
    if attempt == 3:
        print("Your account have been locked")
    else:
        print("Please enter correct username or password")
    attempt = attempt+1

'''
break - Where ever it appears inside the loop, the loop will be terminated there.
continue - That particular iteration will get skipped

'''


