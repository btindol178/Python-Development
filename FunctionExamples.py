# Area of rectangle
def area(a,b):
    return a * b
print(area(3,5))
print(area(a = 3, b = 5)) # this is same thing

# Funciton that takes 2 strings and concatenates them
def foo1(s1, s2):
    return s1 + s2

print(foo1("ok","not"))

# calculate the mean of a series of numbers 
def mean(*args): # gives you a tuple of all the arguments
    return args
print(mean(1,2,3,6,"a"))

# calculate the mean of a series of numbers 
def mean(*args): # gives you a tuple of all the arguments
    return sum(args) / len(args)
print(mean(2,53,5,2,5,3))

# A function that takes an indefinate number of strings as parameters and returns a list conataing all the strings in upper case and sorted alphebetically
def foo2(*args):
    args = [x.upper() for x in args]
    return sorted(args)

print(foo2("snow","bandit","hulk","zeus","rex"))

# To add keyword arguments add two arguments
def mean2(**kwargs):
    return kwargs
#This will give you an output of a dictionary!!!!!!!!!!!!!
print(mean2(a=1,b=2,c=3))

# indefinate number of keyword arguments
def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(x=1, y=2, z=6))

# More functions
def volume(a, b, c):
    return a * b * c
print(volume(30,20,48))

def converter(feet, coefficient = 3.2808):
    meters = feet / coefficient
    return meters
 
print(converter(10))

def find_max(*args):
    return max(args)
print(find_max(3, 99, 1001, 2, 8))


def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)
 
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))