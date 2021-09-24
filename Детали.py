n = int(input())
k = int(input())
m = int(input())
a = k // m
b = k % m
x = k - b
y = int(((x + (x**2)**(1/2))//2) / (x + 1) + 1/2)
res = y * ((n - b)//(x + int(((y - 1)**2)**(1/2)))) * (x//m)
print(res)
