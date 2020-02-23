print("종료하려면 음수를 입력하세요")
sum = 0
cnt = 0
while True:
    grade = input("성적을 입력 하세요")
    grade = int(grade)
    if grade < 0:
        break
    cnt = cnt + 1
    sum = sum + grade
    avr = sum / cnt
str ="%s개의 평균 성적은 %s입니다" % (cnt, avr)
print(str)