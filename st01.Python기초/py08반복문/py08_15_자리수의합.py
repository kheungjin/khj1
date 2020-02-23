
sum= 0
a = input("숫자를 입력하세요 : ")
for x in range(len(a)):
    sum =sum + int(a[x])
str = "%s 숫자의 자리수 합은 %s입니다" % (a, sum)
print(str)