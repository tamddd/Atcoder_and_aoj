n = int(input())
s = input()
lst = []
lst.append([])
for i in s:
    #前回のカッコまでの場所を消したいのだ。
    if i == "(":
        lst.append([])
        lst[-1].append("(")
    elif i == ")":
        if len(lst[-1]) != 0 and lst[-1][0] == "(":
            lst.pop()
        else:
            lst[-1].append(")")
    else:
        lst[-1].append(i)

for i in lst:
    for j in i:
        print(j, end="")
print()
