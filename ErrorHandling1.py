# Errors
def divide(a,b):
    try:
        return a/b
    except:
        return "Zero division is meaningless"

print(divide(10,2))

print(divide(1,0))
