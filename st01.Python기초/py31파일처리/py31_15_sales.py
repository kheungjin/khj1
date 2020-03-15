# 입력 파일 이름과 출력 파일 이름을 받는다.

# 입력과 출력을 위한 파일을 연다.

# 합계와 횟수를 위한 변수를 정의한다.

# 입력 파일에서 한 줄을 읽어서 합계를 계산한다.

# 총매출과 일평균 매출을 출력 파일에 기록한다.
infile = open("./file/sales.txt", "r", encoding="UTF-8")
outfile = open("./file/summary.txt", "w", encoding="UTF-8")
sum = 0
day = 0
while True:
    line = infile.readline()    
    if not line: break
    line = int(line)
    sum = sum + line
    day = day + 1
    print(line)

print("총매출 : ", sum)
print("평균 일매출 : ", sum/day)
list = "총매출 : " + str(sum)
outfile.write(list)

infile.close()
outfile.close()
