# 사용자 함수 만들기
# 일회용 패스워드 생성기를 이용하여서 3개의 패스워드를 생성하여 출력하는 프로그램을 작성해보자. 

def outer_func(tag):  # 1
    text = "Some text "  # 5
    tag = tag  # 6

    def inner_func():  # 7
        str = "<%s> %s </%s>" % (tag, text, tag)  # 9
        return str

    return inner_func  # 8

h1_func = outer_func("h1")   # 2
p_func = outer_func("p")   # 3

print(h1_func())   # 4
print(p_func())    # 10