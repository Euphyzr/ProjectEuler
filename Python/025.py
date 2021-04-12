a, b = 89, 144
n = 12  # 144 is the 12th term

while len(str(b)) != 1000:
    a, b = b, a + b
    n += 1

print(n)