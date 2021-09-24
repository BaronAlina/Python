n=int(input())
m=int(input())
k=m%n
c=(m//n)+k//(abs(k-2))
print(c)
