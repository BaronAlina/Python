import math
x, y=map(float, input().split())
if (x>=0 and x<=math.pi and y>=0 and y<=(math.sin(x)) and y<=0.5):
   print('YES')
else:
   print('NO')
