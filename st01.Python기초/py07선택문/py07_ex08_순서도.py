a = 1
b = 2
c = 0
while c <= 30:
    c = a + b
    a = b
    b = c
str = "c의 값은 %s입니다." % c
print(str)