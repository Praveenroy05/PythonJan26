'''
 Tuple - Is a collection of different data, the datatype can also be different as well,
separated by a comma(,) symbol inside a ().

it is an ordered collection - (1,2,3,4), that means each element inside the list
will have a unique position and the index starts from 0.

Tuple is immutable.



'''

tup1 = ("Rohan", 123, 234.46, "Apple")
tup2 = (1,2,3,4,5)

tup3 = list(tup1)

tup3[1] = "TS"

del tup1

print(tup2)


# Assignment to access the value from the tuple in different way:

# 1. By using Index
# 2. By using slice - from 1 index to other - [startIndex, endIndex]
# 3. By using loop