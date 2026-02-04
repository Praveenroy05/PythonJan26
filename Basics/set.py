'''

set - It is a collection of an element. The datatype of an element can be any type. It is defined inside the
{} separated with a comma(,) symbol.

Set is an unordered collection of unique elements only.

Set is also mutable

Set doesn't have support of Index

list - []
tuple - ()
set - {}

'''

set1 = {1,2,3,4,5} # literal

print(set1)


myset = set([1,2,3,4,"TS"])
print(myset)


set2 = {10,20,30,40,10,20,30}
print(set2)

# how to get all the element from the set

for element in set2:
    print(element)


 # for i in range(len(set2)):
 #     print(set2(i))


set3 = {"TS", "JS", "Python", 1, 2,3}

# Adding element inside the set
set3.add("Java")
print(set3)

# Update the element in set
set3.update([4])
print(set3)

# Remove element from the set

set3.remove("Python")
print(set3)

set3.pop()
print(set3)

set3.discard(30)
print(set3)

set3.remove(30)
print(set3)








