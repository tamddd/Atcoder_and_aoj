n = int(input())
s = []

for i in range(n):
    s.append(list(input()))

dx = [1, 0, 0, -1, 1, 1, -1, -1]
dy = [0, 1, -1, 0, 1, -1, 1, -1]
for i in range(n):
    for j in range(n):
        #8方向に向けて、６回進んでそれが４以上あればOK
        for k in range(8):
            px = dx[k]
            py = dy[k]
            nx = i
            ny = j
            cnt = 0
            ok = 0
            for l in range(6):
                if 0 <= nx < n and 0 <= ny < n:
                    if s[ny][nx] == "#":
                        cnt += 1
                    ok += 1
                nx += px
                ny += py
            if 4<=cnt and ok == 6:
                print("Yes")
                exit()

print("No")
