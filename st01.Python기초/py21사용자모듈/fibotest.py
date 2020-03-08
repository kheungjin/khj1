# import 방식
# 모듈 import : import 모듈이름
# 함수 import : from 모듈이름 import 모듈함수
# as   import

import fibo
def main():
    val = fibo.fib2(10)
    print(val)
# from 모듈이름 import 모듈함수

# 이 모듈이 단독으로 사용되면 main()를 호출하라.
if __name__ == "__main__":
    main()