# x = int(input("x 값 : "))
# y = int(input("y 값 : "))
# if x > y:
#     print("x값이 크다 : ",x)
# else:
#     print("y값이 크다 : ",y)  
# 
# print("종료합니다")  

점수=input("점수는? ")
점수=int(점수)

if 90 <= 점수 <= 100:
    print("A 학점입니다")
elif 80 <= 점수 < 90:
    print("B 학점입니다")
elif 70 <= 점수 < 80:
    print("C 학점입니다")
elif 60 <= 점수 < 70:
    print("D 학점입니다")
else:
    print("F 학점입니다")
