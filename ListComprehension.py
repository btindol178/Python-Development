temps = [221,234,340,230,235] # temperatures stored like this and leave out the 23.4 (leave out period)

# Loop way iterate over the temps and divide by 10 and append then print
new_temps = []
# to get temperature in proper format
for temp in temps:
    new_temps.append(temp/10)

print(new_temps)

# or use list comprehensions!
# list is created dynamically
new_temps = [temp / 10 for temp in temps] # forloop to iterate i is temp and divide by 10 in temps
print(new_temps)

#List comprehension with Conditional statment aspect!
temps2= [-9999,234,340,-230,235] 

new_temps3 = [temp / 10 for temp in temps2 if temp > 0] # forloop to iterate i is temp and divide by 10 in temps

print(new_temps3)

# Takes a list and returns only integers
def foo(lst):
    return [i for i in lst if  isinstance(i,int)]

print(foo([99,"no data", 24,45,"cool",23]))

# Only positive numbers
def foo2(lst):
    return [i for i in lst if i > 0 ]
print(foo2([-4, 10,30,-48,28,4]))

# List comprehension If then statement!
temps4= [-9999,234,340,-230,235,34,5,2334] 
new_temps5 = [temp / 10 if temp != -9999 else 0 for temp in temps4] # forloop to iterate i is temp and divide by 10 in temps
print(new_temps5)

# This function takes a list that contains numbers and strings and returns smae list but with 0 instead of string
def foo3(lst):
    return [i if not isinstance(i, str) else 0 for i in lst ]
    
print(foo3([99,"data",3,"ok",232]))

# Convert and sum up
# This function takes a as parameter a list that contains decimal numbers as strings and returns the sum of those numbers
def foo4(lst):
    return sum([float(i) for i in lst])
print(foo4(['1.2','1.5','1.4','8.8']))

# Few more things
print([i*2 for i in [1, 5, 10]])

print([i*2 for i in [1, -2, 10] if i>0])

print([i*2 if i>0 else 0 for i in [1, -2, 10]])