
# 숫자가 아닌 것을 정수로 변환하려고 할 때
i = int("안녕하세요")
# 숫자가 아닌 것을 실수로 변환 할 때

# 소수점이 있는 숫자 형식의 문자열을 int() 함수로 변환 할 때
try:
    i = int("안녕하세요")
    print(i)
except ValueError:
    pass

f = float("안녕하세요")
try:
    f = float("안녕하세요")
except ValueError:
    pass

w = input("가로 :")
h = input("세로 :")
try:
    area = w * h
    perimeter = 2 *(w+h)
except SyntaxError:
    w = float(w)
    h = float(h)
area = w * h
perimeter = 2 *(w+h)

print("사각형의 넓이 :", area)
print("사각형의 둘레 :", perimeter)