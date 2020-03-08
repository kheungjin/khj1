str = """This was a great help.
I applied this method to similiar problem
and rather than concat a SELECT statement
I created an event scheduled every couple
hours to rebuild a view that pivots n amount
of rows from one table into n columns on the other.
It is a big help because before I was rebuilding
the query using PHP on every execution of the SELECT.
Even though views can not leverage Indexes,
I am thinking filtering performance will not
be an issue as the pivoted rows->columns
represent types of training employees at a
franchise have so the view will not ever break
a few thousand rows."""

str = str.replace("\n", "")
dic =dict()
ll = []
ll = str.split(" ")
check = ""
for i in range(len(ll)):
    val = ll[i][0]
    val = val.upper()
    check = dic.get(val)
    if check == None:
        dic[val] = "-"
    else:
        dic[val] = dic[val] + "-"

for k, v in dic.items():
    print(k, " : ", v)

