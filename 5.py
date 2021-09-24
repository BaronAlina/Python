x, y=map(float, input().split())
if((y <= 0) or (y >= x)) and (x**2 + y**2 <= 1):
    print('YES')
else:
    print('NO')
    
