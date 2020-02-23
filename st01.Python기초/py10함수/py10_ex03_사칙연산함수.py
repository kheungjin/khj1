def add(x, y):
    result = x + y
    return result

def minus(x, y):
    result = x - y
    return result

def mul(x, y):
    result = x * y
    return result

def div(x, y):
    result = x / y    
    return result

a = input("First no : ")
b = input("Second no : ")
a = int(a)
b = int(b)

value = add(a,b)
print("add : ", value)
value = minus(a,b)
print("minus : ", value)
value = mul(a,b)
print("mul : ", value)
value = div(a,b)
print("div : ", value)