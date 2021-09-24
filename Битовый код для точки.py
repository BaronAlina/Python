x, y=map(float, input().split())
if(y<=1):
    print(1, end='')
else:
    print(0, end='')
if(y<=-x):
    print(1, end='')
else:
    print(0, end='')
if(x**2+y**2<=1):
    print(1, end='')
else:
    print(0, end='')
if((x-1)**2+y**2<=1):
    print(1)
else:
    print(0)
    
