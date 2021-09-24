n = int(input())
a = int(n ** 0.5)
print (a)
import random
x = random.randint()
f = ((((a+x)**2)-n)**0.5)
f1 = f % 1
if f1 == 0:
    i = a + x - f
    g = a + x + f
    n1 = i*g
    if n1 == n:
        print (i, g)
        else:
            
        
    


