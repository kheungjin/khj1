
# 작업 순서
# 1. 모듈 또는 클래스 import
# 2. main() 메서드 만들기
#     인스턴스 생성
# 3. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()

# 코딩 하기
import FourCal

num1 = input("첫번째 숫자를 입력하세요 : ")
num2 = input("두번째 숫자를 입력하세요 : ")
num1 = int(num1)
num2 = int(num2)


def main():
    c1 = FourCal.FourCal(num1, num2)
    val = c1.getNum1
    print("num1 = ", val)
    c1.setNum1(8)
    print("Add = ", c1.Add())
    print("Minus = ", c1.Minus())
    print("Mul = ", c1.Mul())
    print("Div = ", c1.Div())


if __name__ == "__main__":
    main()
