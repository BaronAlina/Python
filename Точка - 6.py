x, y=map(float, input().split())
if ((x**2+y**2<=1)):
    if (x>0):
        print ('YES')
    elif(y<=-x) and (y>x):
        print('NO')
    else:
        print ('YES')
else:
    print('NO')
