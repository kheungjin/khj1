
pos = 0
value = ""

#  List 선언
ll = []

#  C: 추가. 검색: "파이썬 리스트 추가"
#  MILK, BREAD, BUTTER 순으로 추가
#
ll.append("milk")
ll.append("bread")#
ll.append("butter")
#  APPLE 삽입. 검색: "파이썬 리스트 삽입"
#  특정 위치에 추가하기
#  "BREAD" 앞에 "APPLE" 삽입
pos = ll.index("butter")
ll.insert(pos,"apple")
#
#  R: 읽기
#  BUTTER 값을 출력하시오.
#  "BUTTER" 가 들어있는 방번호 찾기
#

#  U: 수정. 검색: "파이썬 리스트 수정"
#  "BREAD" 를 "GRAPE"로 변경
#  "BREAD" 가 들어있는 방번호 찾기
#
pos = ll.index("bread")
ll[pos] = "grape"
#  D: 인덱스로 삭제. 검색: "파이썬 리스트 삭제"
#  인덱스를 이용하여 GRAPE 를 삭제
#

#  D: 값으로 찾아서 삭제. 검색: "파이썬 리스트 값으로 삭제"
#  값으로 MILK를 찾아서 삭제하시오
#


#  P: 리스트를 for문으로 출력.
#  검색: "파이썬 리스트 for 출력"
#  검색: "파이썬 리스트 크기"
#

#  P: 리스트를 for-each문으로 출력.
#

#  테스트용 데이터 생성을 위한 코드. 수정하지 마시오.
for i in range(4):
    ll.append("apple")
    ll.append("banna")


#  S: 검색: "파이썬 리스트 검색
#  첫번째 APPLE을 찾으시오.
pos = ll.index("apple")

#  S: 오름차순 정렬. 검색: "파이썬 리스트 오름차순 정렬"
ll.sort()
print(ll)
#  S: 내림차순 정렬. 검색: "파이썬 리스트 내림차순 정렬"
ll.sort(reverse=True)
print(ll)
#  검색2. APPLE 이 몇개 있나요?
count = 0
for i in ll:
    if i == "apple":
        count += 1
print("apple의 수 : ", count)
#  변환된 배열을 for 문으로 출력.



#  list의 모든 값을 while문을 사용하여 삭제하시오
while len(ll) != 0:
    del ll[0]

print(ll)