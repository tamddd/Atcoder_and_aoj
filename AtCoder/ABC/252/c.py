n = int(input())
a = []
for i in range(n):
    a.append(list(input()))
from collections import deque
import heapq
ans = 10010011
for i in range(10):
    #iにする
    i = str(i)
    dct = {}
    st = set()
    lst = []
    for j in range(n):
        cnt = 0
        dq = deque(a[j])
        while dq[0] != i:
            p = dq.popleft()
            dq.append(p)
            cnt += 1
        lst.append(cnt)
    vis = set()
    heapq.heapify(lst)
    while len(lst) != 0:
        m = heapq.heappop(lst)
        if m in vis:
            heapq.heappush(lst, m+10)
        vis.add(m)
    ans = min(m, ans)
    
print(ans)
