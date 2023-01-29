# THIS IS CHALLENGE

# define a function take any no of lists containing number
# [1,2,3] , [4,5,6], [7,8,9]
# return average
# (1+4+7)/3 ,(2,5,8)/3, (3,6,9)/3  


# try to make this anonymous function in one line using lambda
# def average_finder(l1,l2):
#     average = []
#     for pair in zip(l1,l2):
#         average.append(sum(pair)/len(pair))
#     return average

average_finder = lambda *args: [(sum(pair)/len(pair)) for pair in zip(*args)]

print(average_finder([1,2,3] , [4,5,6], [7,8,9]))

#class 162
# any , all function

numbers1 = [13,1,9,7,10]
numbers2 = [1,2,3,4,5,6]

print(any([num%2==0 for num in numbers1]))
print(all([num%2==0 for num in numbers1]))

# evens1 = []
# for num in numbers1:
    # evens1.append(num%2==0)

# print(all([True, False, True, True])) #----> False

#class 163
# any all function

def my_sum(*args):
    # args =()
    if all([(type(arg)==int or type(arg)== float) for arg in args]):
        total = 0
        for num in args:
            total += num
        return total
    else:
        return "Wrong input"

print(my_sum(1,2,3,4,8.9))

#class 164
# advabnce min() and max()

# numbers = [1,2,4,5,7]
# print(min(numbers))


names = ['Harshit Vashisth', 'Moihit', 'ab', 'z']
print(max(names,key = lambda item : len(item)))

students = {
    'harshit' : {'score':50, 'age': 24},
    'mohit' : {'score':75, 'age': 19},
    'rohit' : {'score':76, 'age': 23}
}

print(max(students, key = lambda item : students[item]['age']))

# students2 = [
#     {'name':'harshit','score':90, 'age': 24},
#     {'name':'mohit','score':70, 'age': 19},
#     {'name':'rohit','score':60, 'age': 23},
# ]
# print(max(students2,key = lambda item:item.get('age'))['name'])

#class 165
fruits = ['grapes', 'mango', 'apple']
# sort
# fruits.sort()
# print(fruits)

fruits2 = ('grapes', 'mango', 'apple')
# print(sorted(fruits))


fruits3 = {'grapes', 'mango', 'apple'}
print(sorted(fruits))



guitars = [
    {'model': 'yamaha f310','price':8400},
    {'model': 'faith naptune','price':50000},
    {'model': 'faith apollo venus','price':35000},
    {'model': 'taylor 814ce','price':450000}
]

sorted_guitars = sorted(guitars, key = lambda d:d['price'], reverse = True)
print(sorted_guitars)

#class 166
# what are doc strings
# how to write docstring
# how to see docstring
# what is help function

def add(a,b):
    ''' this function takes 2 numbers and return their sum'''
    return a+b

# print(add.__doc__)

# len , sum , max , min , sorted
# print(len.__doc__)

# print(sum.__doc__)
# sum
print(help(sum))

#class 167
# you have to have a complete understanding of functions,
# first class function / closures
# the finally we will learn about decorators

def square(a):
    return a**2

s = square
# print(s(7))
print(s.__name__)
print(square.__name__)
print(s)
print(square)
#class 168
# map
def square(a):
    return a**2

l = [1,2,3,4]
# print(list(map(lambda a: a**2,l)))

def my_map(func, l):
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list  

def my_map2(func, l):
    return [func(item) for item in l] 

print(my_map2(lambda a : a**3,l))
#class 169
# functions returning function

def outer_func():
    def inner_func():
        print('inside inner func')
    return inner_func

def outer_func2(msg):
    def inner_func2():
        print(f"message is {msg}")
    return inner_func2

var = outer_func2("hello there ! ")
var()
#class 170
# function returning function (closure) practice

def to_power(x): # x = 3
    def calc_power(n): # n =2
        return n**x
    return calc_power

cube = to_power(3)
print(cube(2))

square = to_power(2)
print(square(4))