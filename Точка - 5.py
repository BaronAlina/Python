x, y=map(float, input().split())
if ((x*x+y*y<=1) and (y>=x)) or ((x*x+y*y<=1) and (x<=0)):
    print ('YES')
else:
    print('NO')
