
'''

# List  - Is a collection of different data, the datatype can also be different as well,
seperated by a comma(,) symbol inside a [].
# it is an ordered collection - [1,2,3,4], that means each element inside the list
will have a unique position and the index starts from 0.

# It can be mutable (Changable)

# List also allows the duplicate values

Example -  1 is available at 0th Position

Syntax:

variableName = [data1,data2,data3,data4]

// TO access the value from the list you can use index along with the name of the list

Syntax:

listName[startIndex : EndIndex]

'''


list1 = ["Python", "JS", 123, True, 123.45, "JS", 123]
print(list1)

print(list1[0]) # to access single value
print(list1[1:5]) # slice from one index to other

# How do we access the complete data from list

# print(list[0])
# print(list[1])

for element in list1:
    print(element)


print(list1[1]) # JS

list1[1] = "Typescript"
print(list1[1])


# Delete the element from the list using index
del list1[1]
print(list1)

 # To Add element inside the list


# append - add the element to the end of a list
list1.append("Java")
print(list1)

# Add the element to a specific index inside alist  - insert(index, element)
list1.insert(2, "Apple")
print(list1)

# How to add 2 diff list

list2 = [10,20,30]

#list1+list2

list1.extend(list2)
print(list1)


# Delete the element from the list by using direct element - remove(Element)

list1.remove("Java")
print(list1)

# pop() - Which deletes the last element from the list
list1.pop()
print(list1)
list1.pop(0)
print(list1)

# clear() - Which will remove all the elements from the list
list1.clear()
print(list1)


'''
# Declare a list - ["Login", "Logout", "cart", "payment"]
# result = ["PASS", "FAILED", "PASS", "FAILED"]

# Write a program to collected all the failed test cases from based on the result

# failed_test = ["Logout", "Payment"]

'''








