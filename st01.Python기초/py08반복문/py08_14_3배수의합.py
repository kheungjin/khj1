i = 1
sum = 0
while i <= 100:
    rem = i % 3
    if rem == 0:
        sum = sum + i
    i = i + 1    
str ="%s부터 %s사이 3의 배수의 합은 %s입니다" % (1,100,sum)
print(str)
