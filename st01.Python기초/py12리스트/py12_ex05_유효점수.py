
# step1. ArrayList 인스턴스, list  만들기.
# step2. 심사 위원수를 입력 받는다.   
# step3. 심사 위원의 점수 입력 받아서 list에 저장. 
#     몇 번 입력 받아야 하는가? 심사 위원수 만큼
# step4. 합계를 구하는 메서드 만들기
#     1번방부터 마지막방 -1 까지 
# step5. 평균을 구하는 메서드 만들기. 
#     평균값 = (double)sum / ( list.size() - 2 ) 
# step6. ArrayLis 정렬하기.
# step7. 합계를 구하고 출력한다.
# step8. 평균을 구하고 출력한다.


ll = []
no = 0
while no < 3:
 심사위원수 = int(input("심사위원의 수를 입력하세요 : "))
 if 심사위원수 >= 3:
     break
    
h_val = 0
for i in range(0,심사위원수,1):
    h_val = int(input("심사위원의 점수을 입력하세요 : "))    
    ll.append(h_val)

ll.sort()
print(ll)
del ll[len(ll)-1]
del ll[0]
print("유효점수 : ", end= " ")
for i in ll:
    print(i, end=" ")
print()

print("합계 : ", sum(ll))
print("평균 : ", round(sum(ll)/len(ll),2))