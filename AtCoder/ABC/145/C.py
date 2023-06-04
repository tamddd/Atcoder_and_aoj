import itertools
import math

n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

ans = 0
c = 0
for p in itertools.permutations(lst):
    now_x = p[0][0]
    now_y = p[0][1]
    c+=1
    total = 0
    for j in p[1:]:
        x = j[0]
        y = j[1]
        total += math.sqrt((now_x-x)**2 + (now_y - y)**2)
        now_y = y
        now_x = x
    ans += total

print(ans/c)
