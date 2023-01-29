# class variable
# circle
# area
# circum
class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def calc_circumference(self):
        return 2*Circle.pi*self.radius


c = Circle(4)
c1 = Circle(5)
print(c1.calc_circumference())

class Laptop:
    discount_percent = 10
    def __init__(self, brand, model_name, price):
        #instance variables
        self.brand = brand
        self.name = model_name
        self.price = price
        self.laptop_name = brand + " " + model_name
    
    def apply_discount(self):
        # self.price
        off_price = (Laptop.discount_percent/100)*self.price
        return self.price - off_price



laptop1 = Laptop('hp', 'au114tx', 63000)
laptop2 = Laptop('apple', 'mackbook pro', 230000)
print(laptop2.apply_discount())

#class 193
# change class variable
# how to print name space for objects
# what if we use self instead of class name for class variables
# 

class Laptop:
    discount_percent = 10
    def __init__(self, brand, model_name, price):
        #instance variables
        self.brand = brand
        self.name = model_name
        self.price = price
        self.laptop_name = brand + " " + model_name
    
    def apply_discount(self):
        # self.price
        off_price = (self.discount_percent/100)*self.price
        return self.price - off_price



laptop1 = Laptop('hp', 'au114tx', 63000)
laptop2 = Laptop('apple', 'mackbook pro', 230000)
laptop2.discount_percent = 50
print(laptop2.__dict__)
print(laptop2.apply_discount())

#class 194
class Person:
    count_instance = 0
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.person_first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('Harshit','Vashistha',24)
p2 = Person('Harshit','Vashistha',24)
p2 = Person('Harshit','Vashistha',24)
print(Person.count_instance)

#class 196
# class methods
# difference between claass methods and instance methods

class Person:
    count_instance = 0 # class variable / class attribute
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instances of {cls.__name__} class"

    def full_name(self):
        return f"{self.full_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18

p1 = Person('Harshit','Vashistha',10)
p2 = Person('Harsh', 'Vashistha', 24)
print(Person.count_instances())

#class 197
# class method as a constructor
class Person:
    count_instance = 0 # class variable / class attribute
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)

    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instances of {cls.__name__} class"

    def full_name(self):
        return f"{self.full_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18



p1 = Person('Harshit','Vashistha',10)
p2 = Person('Harsh', 'Vashistha', 24)

p3 = Person.from_string('Harshit,vashisth,24')
print(p3.full_name())

#class 198
# class method as a constructor
class Person:
    count_instance = 0 # class variable / class attribute
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)

    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instances of {cls.__name__} class"

    @staticmethod
    def hello():
        print('hello, static method is called')

    def full_name(self):
        return f"{self.full_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18



p1 = Person('Harshit','Vashistha',10)
p2 = Person('Harsh', 'Vashistha', 24)

p3 = Person.from_string('Harshit,vashisth,24')

#class 199
# In this video we will talk about
# Encapsulation
# Abtraction
# Some special naming convention
# Name Mangling, __name (not a covenntion)


class Phone:
    def __init__(self, brand,model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.__price = price

    def make_a_call(self, phone_number):
        print(f"callinfg {phone_number} .....")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def send_message(self):
        pass # twilio

phone1 = Phone('nokia','1100',1000)
# print(phone1.__price)
print(phone1._Phone__price)
print(phone1.__dict__)


# phone1._price = -1000
# print(phone1._price)

# _name # convention of private name
# __name__ # dunder/magic methods

#class 200
# will discuss three problems in existing
# the we will solve them using getter , setter decorator 


class Phone:
    def __init__(self, brand,model_name, price):
        self.brand = brand
        self.model_name = model_name
        # self._price = max(price,0)
        # if price > 0:
        #     self._price = price
        # else:
        #     self._price = 0
        # self.complete_specification = f"{self.brand} {self.model_name} and price is {self._price} "

    @property 
    def complete_specification(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0)

    def make_a_call(self, phone_number):
        print(f"callinfg {phone_number} .....")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

phone1 = Phone('Nokia','1100',1000)

phone1._price = -500
print(phone1.brand)
print(phone1.model_name)
print(phone1.price)
print(phone1.complete_specification)

#class 201
class Phone: # base class / parent class
    def __init__(self, brand,model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self, number):
        print(f"calling {number} .....")


class Smartphone(Phone): # derived / child class
    def __init__(self, brand,model_name, price,ram,internal_memory,rear_camera):
        # two ways
        # Phone.__init__(self,brand,model_name,price) uncommon way
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

phone = Phone('nokia', '1100', 1000)
smartphone = Smartphone('onePlus','5',30000,'6 GB','64GB','20MP')
print(phone.full_name())
print(smartphone.full_name() + f"and price is {smartphone._price}")

#class 202
class Phone: # base class / parent class
    def __init__(self, brand,model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self, number):
        print(f"calling {number} .....")


class Smartphone(Phone): # derived / child class
    def __init__(self, brand,model_name, price,ram,internal_memory,rear_camera):
        # two ways
        # Phone.__init__(self,brand,model_name,price) uncommon way
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

phone = Phone('nokia', '1100', 1000)
smartphone = Smartphone('onePlus','5',30000,'6 GB','64GB','20MP')
print(phone.full_name())
print(smartphone.full_name() + f"and price is {smartphone._price}")

#class 203
# Multiple Inheritance

class A:

    def class_a_methods(self):
        return 'I\'m just a class A method'

    def hello(self):
        return 'hello from class A'

class B:

    def class_a_methods(self):
        return 'I\'m just a class B method'

    def hello(self):
        return 'hello from class B'

class C(A,B):
    pass

instance_c = C()
# print(instance_c.class_a_methods())
# print(instance_c.class_b_methods())
# print(instance_c.hello())
# print(help(C))
# print(C.mro())
print(C.__mro__)