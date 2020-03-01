
# 1. List 만들기.
# 2. 학생수 입력 받기. 최소 3명이상
# 3. 학생 성적 입력 받기. 몇번 입력받아야 하는가?
# 4. list에 입력 받은 학생 성적을 추가한다.
# 5. 3번 학생의 성적을 100점으로 바꾸시오.
# 6. list에서 마지막 학생 삭제.
# 7. list에서 0번 값을 출력하시오.
# 8. 평균을 구하고 출력.

ll = []
no = 0
while no < 3:
 학생수 = int(input("학생수를 입력하세요 : "))
 if 학생수 >= 3:
     break
    
h_val = 0
for i in range(0,학생수,1):
    h_val = int(input("성적을 입력하세요 : "))    
    ll.append(h_val)

ll[2] = 100
del ll[no-1]
print(ll[0])
print(sum(ll)/len(ll))