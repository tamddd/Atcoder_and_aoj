import sys
sys.setrecursionlimit(10**7)
n = int(input())
d = {}
for i in range(n):
    t, k, *a = map(int, input().split())
    d[i] = [t, a]

al = set()
total = 0
def f(now):
    global al, total
    if now in al:
        return
    else:
        al.add(now)
        total += d[now][0]
        for i in d[now][1]:
            f(i-1)

f(n-1)
print(total)
