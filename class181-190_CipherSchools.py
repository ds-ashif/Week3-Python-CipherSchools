def even_generator(n):
    for num in range(2,n+1,2):
        yield(num)

even_nums = even_generator(20)
for num in even_nums:
    print(num)

#class 183
square = (i**2 for i in range(1,11))

print(next(square))
print(next(square))
print(next(square))


for num in square:
    print(num)

for num in square:
    print(num)

#class 184
import time
# list vs generator
# memory usage , time
# when to use list , when to use generator

# t1 = time.time()
# l = [i**2 for i in range(10000000)] #10million
# print(time.time() - t1)

t1 = time.time()
g = (i**2 for i in range(10000000)) #10million
print(time.time() - t1)

#class 186
# OBJECTIVES
# WHAT IS CLASS
# HOW TO CREATE AN CLASS
# WHAT IS INIT METHOD , CONSTRUCTOR
# WHAT ARE THE ATTRIBUTES , INSTANCE VARIABLES
# HOW TO CREATE OUR OBJECT

class Person:
    def __init__(self, first_name, last_name, age):
        # instance variables
        print('init method called')
        self.person_first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('Harshit','Vashistha',24)
p2 = Person('Mohit', 'Vashistha', 19)

print(p1.person_first_name)
print(p2.person_first_name)

#class 187
class Laptop:
    def __init__(self, brand, model_name, price):
        #instance variables
        self.brand = brand
        self.name = model_name
        self.price = price
        self.laptop_name = brand + " " + model_name


laptop1 = Laptop('hp', 'au114tx', 63000)
print(laptop1.laptop_name)

#class 189
# instance methods
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.full_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18

p1 = Person('Harshit','Vashistha',24)
p2 = Person('Mohit', 'Vashistha', 19)
print(p1.is_above_18())
# print(p2.full_name())

# l = [1,2,3]
# clear , pop 
# l.clear()
# list.clear(l)
# print(l)
# list.append(l,10)
# print(l)

#class 190
class Laptop:
    def __init__(self, brand, model_name, price):
        #instance variables
        self.brand = brand
        self.name = model_name
        self.price = price
        self.laptop_name = brand + " " + model_name
    
    def apply_discount(self,num):
        # self.price
        off_price = (num/100)*self.price
        return self.price - off_price



laptop1 = Laptop('hp', 'au114tx', 63000)
laptop2 = Laptop('apple', 'mackbook pro', 230000)
print(laptop2.apply_discount(5))