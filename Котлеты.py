k=int(input())
m=int(input())
n=int(input())
kn=n*2//k
if n<=k:
    print(2*m)
elif n*2%k==0:
    mn=kn*m
    print(mn)
else:
    mn=((n*2//k)+1)*m
    print(mn)
    

