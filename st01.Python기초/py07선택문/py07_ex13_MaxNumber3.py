a1 = input('첫번째 값? :')
a2 = input('두번째 값? :')
a3 = input('세번째 값? :')
a1 = int(a1)
a2 = int(a2)
a3 = int(a3)

if a1 >= a2:
    if a1 >= a3:
        print("첫번째 값이 가장 크다", a1)
    else:
        print("세번째 값이 가장 크다", a3)
else:
    if a2 >= a3:  
        print("두번째 값이 가장 크다", a2)
    else:
        print("세번째 값이 가장 크다", a3)

print("===========================")

if (a1 >= a2 and a1 >= a3):
    print("첫번째 값이 가장 크다 : ", a1)
elif (a2 >= a3):
    print("두번째 값이 가장 크다 : ", a2)
else:
    print("세번째 값이 가장 크다 : ", a3)