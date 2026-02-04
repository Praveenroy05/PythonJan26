'''

Dictionary -

1. It is a collection of key-pair inside {}. Both key and value pair will be separated with (:)
{key : value, key1:value1}
2. It is an unordered  and mutable.
3. Key - Key inside the dictionary will always be in unique
4. Value - Can be duplicate as well


'''

dict1 = {"name": "Rahul", "age": 20, "gender": "male"}
dict2 = {1: "name", 2: "age", 3: "age"}

print(dict1)

# Syntax for fetching the value from the dictionary
# dictionary[key]

print(dict1["age"])
print(dict2[2])

# way - 2

# get(key)
# Syntax: dictionary.get(key)
print(dict1.get("gender"))


# - abcdabcdabcd - a3b3c3d3

# # 1. has_key(key)
# print(dict1.has_key(key))


# 1. keys() - Return all the key that are available inside the dict
# 2. values() - Return all the values from the dict
# 3. items() - key-value

print(dict1.keys())
print(dict1.values())
print(dict1.items())


# dict1 = {"name": "Rahul", "age": 20, "gender": "male"}

'''
name
age
gender

Rahul
20
male



name : rahul
age :20
gender : male

'''

for key in dict1:  # dict1.keys() - [name, age, gender]
    print(key, dict1[key])

# Note - By default "key" as a variable inside for loop will refer the key inside dictionary

for value in dict1.values():
    print(value)

for key, value in dict1.items():   # [(key, value)]
    print(key," : ",value)


# Add the elements inside the dictionary

dict1["address"] = "Delhi"
print(dict1)


dict1["address"] = "NY"
print(dict1)


# del dict1["address"]
#
# print(dict1)
#
# # pop(key)
#
# dict1.pop("age")
# print(dict1)

# popitem()
dict1.popitem()
print(dict1)


#clear - clear the complete dictionary
dict1.clear()
print(dict1)



# - How do we work files - text
# - Class -


