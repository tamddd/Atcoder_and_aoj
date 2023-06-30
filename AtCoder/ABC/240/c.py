n, x = map(int, input().split())

st = set()
st.add(0)
for i in range(n):
    new_st = set()
    a, b = map(int, input().split())
    for i in st:
        new_st.add(a+i)
        new_st.add(b+i)
    st = new_st
#setで管理すればいい？
print(st)
if x in st:
    print("Yes")
else:
    print("No")
