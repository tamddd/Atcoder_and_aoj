n = int(input())

dp = [[0 for i in range(10100)] for j in range(n+1)]
dp[0][0] = 1

a = []
for i in range(n):
    a.append(int(input()))

for i in range(n):
    for j in range(10100):
        if dp[i][j]:
            dp[i+1][j] = 1
            dp[i+1][j+a[i]] = 1

ans = 0
for i in range(10100):
    if i % 10 != 0 and dp[n][i]:
        ans = max(ans, i)
print(ans)
