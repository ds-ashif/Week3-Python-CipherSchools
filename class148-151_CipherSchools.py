# kwargs (keyword arguments)
# **kwargs (double star operator)

# kwargs as a parameter
def func(**kwargs):
    for k,v in kwargs.items():
        print(f'{k} : {v}')

# dictionary unpacking
d= {'name':'Harshit', 'age':24}
func(**d)

#class 149
# functions with all parameters
# very important to understand

# PADK

# parameters
# *args
# default parameters
# **kwargs

def func(name, *args, last_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('harshit', 1,2,3, a=1, b=2)

#class 150-151
# function 
# list , reverse_str = True
# list

def func(l, **kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]


names = ['harshit', 'mohit']
print(func(names, reverse_str = True))