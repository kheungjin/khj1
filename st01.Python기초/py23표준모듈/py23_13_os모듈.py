
# 모듈을 읽어 들입니다.
import os
# 기본 정보를 몇 개 출력해봅시다.

# 폴더를 만들고 제거합니다[폴더가 비어있을 때만 제거 가능].

# 파일을 생성하고 + 파일 이름을 변경합니다.

# 파일을 제거합니다.



# 파일 존재 유무 체크 
# os.path.isfile()
# 1. 상대경로 사용
#   ../ 부모폴더
#   ./  현재폴더
# 2. 절대경로 사용
#   c:\intel\aa.txt
#   d:\intel\bb.txt 

print(os.getcwd())
print(os.getcwd())
if os.path.isfile("./st01.Python기초/py23표준모듈/proverbs.txt"):
    print("파일이 존재")
else:
    print("파일이 부재")
# 현재 폴더의 파일/폴더를 출력합니다.

# 현재 폴더의 파일/폴더를 구분합니다.

# 폴더를 읽어 들이는 함수
