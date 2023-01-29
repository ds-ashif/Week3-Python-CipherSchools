# Decorators - enhance the functionality of other functions
# @ use for decorator

def decorator_function(any_function):
    def wrapper_function():
        print('this is awesome function')
        any_function()
    return wrapper_function

# this is awesome function

@decorator_function #shortcut
def func1():
    print('this is function 1')

func1()

@decorator_function
def func2():
    print('this is function 2')

func2()

# func1 = decorator_function(func1)
# func1()

#class 172
def decorator_function(any_function):
    def wrapper_function(*args, **kwargs):
        print('this is awesome function')
        return any_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def func(a):
    print(f'this is function with argument {a}')

func(5)

@decorator_function
def add(a,b):
    return a+b

print(add(2,3))

#class 173
from functools import wraps
def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args, **kwargs):
        """ this is wrapper function """
        print('this is awesome function')
        return any_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def add(a,b):
    ''' this is add function'''
    return a+b

print(add.__doc__)
print(add.__name__)

#class 174
from functools import wraps

def print_function_data(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"You are calling {function.__name__}")
        print(f"{function.__doc__}")
        return function(*args, **kwargs)
    return wrapper


@print_function_data
def addition(a,b):
    '''This function takes two numbers as arguments and return their sum'''
    return a+b

print(addition(4,5))
# output
# you are calling add function
# This function takes two numbers as parameters and return their sum
# 9

#class 175
# exercisse decorator
import time

t1=time.time()
print("this is line one")
x=5
if x==5:
    print('x is equal to 5')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
t2=time.time()
print(t2-t1)

#class 176
from functools import wraps
import time
def calculate_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f'Executing .... {function.__name__}')
        t1=time.time()
        returned_value = function(*args, **kwargs)
        t2 = time.time()
        total_time = t2-t1
        print(f'This function took {total_time} seconds')
        return returned_value
    return wrapper
    
@calculate_time
def square_finder(n):
    return [i**2 for i in range(1,n+1)]

square_finder(1000)

#Class 177
from functools import wraps
def only_int_allow(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if all([type(arg) == int for arg in args]):
            return function(*args, **kwargs)
        # data_types = []
        # for arg in args:
        #     data_types.append(type(arg)==int)
        # if all(data_types):
        #     return function(*args, **kwargs)
        else:
            print("Invalid argument")
    return wrapper



@only_int_allow
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total


print(add_all(1,2,3,4,5))
#class 178
from functools import wraps
def only_data_type_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([type(arg) == data_type for arg in args]):
                return function(*args, **kwargs)
            print("Invalid argument")
        return wrapper
    return decorator

@only_data_type_allow(str)
def string_join(*args):
    string = ''
    for i in args:
        string += i
    return string

print(string_join('harshit', 'Vashisth', 'a'))

#class 179
# generators
# generators are iterators

# iterator , iterable

l = [1,2,3] # iterable

# for i in l:
    # print(i)

# i = iter(l)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# next(l)


# for num in map(lambda a :a**2, l):
    # print(num)

# l= [1,4,9,16]
# memory ----- [..................................] , list
# memory ---- (5)


#class 180
# Create your first generator with generator function
# 1.) generator function

# 10 , 1 to 10

def nums(n):
    for i in range(1,n+1):
        yield(i)

numbers = nums(10)

for num in numbers:
    print(num)

for num in numbers:
    print(num)


# memory -------> [..............] lists