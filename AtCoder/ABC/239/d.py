a, b, c, d = map(int, input().split())

#ある数に対して、何を足しても素数にならないならOK
prime_nums = set()
limit = 201
for i in range(2, limit):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_nums.add(i)

for i in range(a, b+1):
    lst = []
    for j in range(c, d+1):
        lst.append(i + j)
    flg = True
    for k in lst:
        if k in prime_nums:
            flg = False

    if flg:
        print("Takahashi")
        exit()
print("Aoki")
