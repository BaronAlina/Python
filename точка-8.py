x, y=map(float, input().split())
if(x>=0):
    if(y<=1):
        if(x*x + y*y <= 1) and (y >= x-1):
            print('YES')
else:
    print('NO')

    
