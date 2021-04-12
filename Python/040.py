l = "".join(str(n) for n in range(1, (10 ** 6 + 1)))
ans = 1
for i in (10 ** exp for exp in range(7)):
    ans *= int(l[i-1])

print(ans)