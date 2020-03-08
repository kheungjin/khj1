import math
def calCircle(r):
    area = math.pi * r * r
    circum = 2 * math.pi * r
    return(area,circum)

def main():
    radius = float(input("원의 반지름을 입력하시오 : "))
    (a, c) = calCircle(radius)
    tmp = "원의 둘레는 %10.4f, 둘레는 %10.4f 이다" % (a, c)
    print(tmp)

if __name__ == "__main__":
    main()