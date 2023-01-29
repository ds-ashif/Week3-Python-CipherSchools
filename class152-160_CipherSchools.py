def add(a,b):
    return a+b

def new_add(*args):
    # 1,2,3,4
    # (1,2,3,4)
    total = 0
    for num in args:
        total+= num
    return total


# print(new_add(1,2,3))

# l=(1,2,3,4)
# print(new_add(*l))

# kwargs - keyword arguments , **
# def func(**kwargs):
    # print(kwargs) #gather as dictionary
    # print(type(kwargs))

# func(name = 'harshit', age = 24)

# kwargs , args , normal, default
# PADK - parameter , args , default , kwargs

def func2(name, *args, last_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func2('harshit', 1,2,3, a=1, b=2)

#class 153
# lambada expressions (anonymous function)

def add(a,b):
    return a+b

add2 = lambda a,b : a+b
print(add2(2,3))


multiply = lambda a,b : a*b
print(multiply(2,3))

print(add)
print(add2)
print(multiply)

#class 154
# lambda expression practice
# def is_even(a):
#     return a%2==0 #a%2 ==0 -----> true, false

# print(is_even(5))

# iseven2 = lambda a : a%2==0
# print(iseven2(6))

# def last_char(s):
#     return s[-1]

# last_char = lambda s : s[-1]
# print(last_char('harshit'))

# lambda with if , else
def func(s):
    return len(s)>5


func = lambda s : len(s) > 5
print(func('abcdefg'))
#class 155
# we use enumerate function with for loop to track position of our
# item in iterable


# How we can do this without enumerate function
names = ['abc', 'abcdef', 'harshit']
# # 0 -- 'abc'
# # 1 -- 'abcdef'
# pos = 0
# for name in names:
#     print(f"{pos} ---> {name}")
#     pos+=1


# with enumerate function

# for pos,name in enumerate(names):
    # print(f"{pos} ---> {name}")




# Define a function that take two arguments
# 1.) list containing string
# 2.) string that want to find in your list
# and this function will return the index of string in your list and
# if string is not present then return -1

def find_pos(l, target):
    for pos, name in enumerate(l):
        if name== target:
            return pos
    return -1

print(find_pos(names, 'harshit'))

#class 156
# map function

numbers = [1,2,3,4]

def square(a):
    return a**2

squares = list(map(lambda a:a**2, numbers))
print(squares)

# list comp
squares_new = [i**2 for i in numbers]
print(squares_new)

new_list = []
for num in numbers:
    new_list.append(square(num))

print(new_list)

names = ['abc', 'abcd', 'abcde']
length = list(map(len,names))

print(length)

#class 157
# filter function

def is_even(a):
    return a%2==0

numbers = [3,4,2,1,5,6,9,8,10]

evens = filter(lambda a:a%2==0, numbers)

new_even = [i for i in numbers if i%2==0]

print(list(evens))
print(new_even)

#class 158
# iterator vs iterables

numbers = [1,2,3,4] #, tuples, strings --- iterables
squares = map(lambda a:a**2, numbers) # iterator

print(next(numbers))

#class 159
# zip function
user_id = ['user1', 'user2', 'user3']
names = ['harshit', 'mohit', 'rohit']
last_names = ['vashistha', 'vashishtha','sharma']

# ('user1','harshit'),('user2','mohit')
print(list(zip(user_id, names, last_names)))

# example =[('a',1), ('b', 2)]
# print(dict(example))

#class 160
l1 =[1,3,5,7]
l2 =[2,4,6,8]
new_list = []

# l =[(1,2), (3,4), (5,6), (7,8)]
# *operator with zip

# l1, l2 = list(zip(*l))
# print(list(l1))
# print(list(l2))
for pair in zip(l1,l2):
    new_list.append(max(pair))

print(new_list)