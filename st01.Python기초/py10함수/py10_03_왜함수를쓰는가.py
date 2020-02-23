sum1 = 0
for x in range(1, 11, 1):
    sum1 = sum1 + x
str = "%s부터 %s까지 합은 %s" % (1, 10, sum1)
print(str)

sum2 = 0
for x in range(1, 101, 1):
    sum2 = sum2 + x
str = "%s부터 %s까지 합은 %s" % (1, 100, sum2)
print(str)

sum3 = 0
for x in range(100, sum2+1, 1):
    sum3 = sum3 + x
str = "%s부터 %s까지 합은 %s" % (100, sum2, sum3)
print(str)

#함수 만들기
def get_sum(xx,yy):
    sum3 = 0
    for x in range(xx, yy+1, 1):
        sum3 = sum3 + x
    str = "함수출력: %s부터 %s까지 합은 %s" % (xx, yy, sum3)
    print(str)
    return sum3

#함수호출
sum1=get_sum(1,10)
sum2=get_sum(1,100)
sum3=get_sum(100,sum2)