n = int(input())
h = str((n // 3600) % 24)
x = n - ((n // 3600) * 3600) 
m0 = str((x // 60) // 10)
m1 = str((x // 60) % 10)
s0 = str((x % 60) // 10)
s1 = str((x % 60) % 10)
print(h, m0 + m1, s0 + s1, sep = ':')
