n = int(input())
k = int(input())
n2=n//2
if 1<=k<=n<=50 and n%2 == 0:
    if n == 2:
        x = 0
    elif k <= n2:
        x = n - 3 - (k-1)
    elif k > n2:
        x = n - 3 - (n-k)
 
    print(x)
