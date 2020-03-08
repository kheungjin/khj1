inw = input("문자열을 입력하세요: ")

table = {"B4" : "Before",
         "TX": "Thanks",
         "BBL": "be Back Later",
         "BCNU": "Be Seeing You",
         "HAND": "Have A Nice Day",
         }

ll = []
ll = inw.split(" ")
result =""
for i in ll:
    value = table.get(i)
    if value == None:
        result = result + i + " "
    else:
        result = result + value + " "
print(result)
    