# list comprehension with if else
nums = [1,2,3,4,5,6,7,8,9,10]
# new_list = [-1,4, -3, 8]

new_list = []
for i in nums:
    if i%2 == 0:
        new_list.append(i*2)
    else:
        new_list.append(-i)
print(new_list)

new_list2 = [i*2 if (i%2 == 0) else -i for  i in nums]
print(new_list2)

#class 138
# list comprehension in nested list

example = [[1,2,3],[1,2,3],[1,2,3]]

nested_comp = [[i for i in range(1,4)] for j in range(3)]
print(nested_comp)

new_list = []
for j in range(3):
    new_list.append([1,2,3])

#class 139
# LIST COMPREHENSIOM SUMMARY
# square = []
# for i in range(1,11):
#     square.append(i**2)

# square = [i**2 for i in range(1,11)]
# print(square)

# even_num = [i for i in range(1,11) if i % 2 == 0]
# print(even_num)

# if else
# [1,2,3,4,....10]
# [-1, 4, -3, 8]
# mixed = [i*2 if (i%2==0) else -i for i in range(1,11)]
# print(mixed)
nl = [[1,2,3], [1,2,3], [1,2,3]]
new_list = [[i for i in range(1,4)] for j in range(3)]
print(new_list)
new_list2 = []
for j in range(3):
    new_list.append([1,2,3])

#class 140
# dictionary comprehension
# square ={1:1, 2:4, 3:9}
square = {f"Square of {num} is":num**2 for num in range(1,11)}
for k,v in square.items():
    print(f"{k} : {v}")

string = "Harshit"
# for i in string:
    # print(i)
# {'H' : 2 , 'a' : 1}
word_count = {char:string.count(char) for char in string}
print(word_count)

#class 141
# dictionary comprehension with if else
# d = {1:'odd' , 2:'even'}
odd_even = {i:('even' if i%2==0 else 'odd') for i in range(1,11)}
print(odd_even)

#class 142
# sets comprehension -----> only one video
s = {k**2 for k in range(1,11)}
print(s)

names = ['harshit', 'mohit', 'rohit']
first = {name[0] for name in names}
print(first)

#class 143
# make flexible functions

# *operator
# *args

def total(a,b):
    return a+b

def all_total(*args):
    # (1,2,3,4,5,65)
    total = 0
    for num in args:
        total += num
    return total

print(all_total(1,2,3,4))

#class 144
# *args with normal parameter

def multiply_nums(num,*args):
    multiply = 1
    # print(num)
    print(args)
    for i in args:
        multiply *= i
    return multiply

print(multiply_nums(2,4,3,4))

#class 145
def multiply_nums(*args):
    multiply = 1
    print(args) # ([2,3,4])
    for i in args:
        multiply *= i
    return multiply

nums = (2,3,4)
print(multiply_nums(*nums)) #unpack