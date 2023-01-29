d={'name' : 'harshit', 'age' : 24}

# or
d1=dict(name = 'harshit',age = 24)

# or

d2={
    'name' : 'harshit', 
    'age' : 24,
    'fav_movies' : []
}


# how to acces data from dictionary
# you cannot do like
# d[0] , because ther is no order inside dictionary

# syntax
# print(dictname[keyname])
print(d['name'])


# add data inside empty dict
empty_dict={}
empty_dict['key1'] = 'value1'
empty_dict['key2'] = 'value2'
# print(empty_dict)

# check existence of value inside dict
# use in keyword to check for keys



# how to iterate over dictionary
# most common method
# for key, value in d.items():
#        print(f'key is {key} and value is {value}')

# to print all keys

# for i in d:
#     print(i)

# to print all values
# for i in d.values():
    # print(i)


# most common dict methods

# get method
# to access a key and check existance
# print(d.get('name)) 

# Q - why we use get
# A - to get rid of error
# example
# print(d['names])
print(d.get('names'))


# to delete item
# pop ----> take one argument which is keyname

# popped = d.pop('name')
# print(popped)
# print(d)

# popitem
popped = d.popitem()
print(popped)
print(d)

#class 129
# set data type
# unordered collection of unique items

s={1,2,3}

s={1,1.0,2.3, 'string'} #cannot store list and dictionary in it

# print(s[1])
# l=[1,2,3,4,5,5,5,6,7,7,8]
# remove duplicate
# s2=list(set(l))
# print(s2)
# s.add(4)
# s.add(5)
# s.add(4)
# s.remove(3)
# s.discard(5)
# s1 = s.copy()
# print(s1)
print(s)

#class 130
# in keyword in sets and for loop

s = {'a', 'b', 'c'}

# in keyword to check if item is present or not in set
if 'a' in s:
    print("present")
else:
    print("not present")

# for loop
for item in s:
    print(item)
# set maths
s1={1,2,3,4}
s2={3,4,5,6}

# union
# intersection

# {1,2,3,4,5,6}
# 
# union_sets = s1|s2
# print(union_set)
print(s1 & s2)

#class 131
# list comprehension
# with the help of list comprehension we can create of list in one line

# create a list of squares from 1 to 10
# squares=[]
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)

# squares2 = [i**2 for i in range(1,11)]
# print(squares2)

# negative = []
# for i in range(1,11):
#     negative.append(-i)
# print(negative)

# new_negative = [-i for i in range(1,11)]

names = ['Harshit', 'Mohit', 'Rohit']
# new_list = ['H', 'M', 'R']
# new_list = []
# for name in names:
#     new_list.append(name[0])
# print(new_list)

new_list2 = [name[0] for name in names]
print(new_list2)

#class 132
def reverse_strings(l):
    return [name[::-1] for name in l]

print(reverse_strings(['abc', 'tuv', 'xyz']))

def reverse_str(l):
    new_list = []
    for name in l:
        new_list.append(name[::-1])
    return new_list

print(reverse_strings(['abc', 'tuv', 'xyz']))