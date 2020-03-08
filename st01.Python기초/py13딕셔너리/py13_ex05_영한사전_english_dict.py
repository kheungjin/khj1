dic = dict()
dic["one"] = "하나"
dic["two"] = "둘"
dic["three"] = "셋"
word = input("단어를 입력하세요 : ")
print(dic.get(word, "없음"))