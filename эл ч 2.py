x1=int(input())
y1=int(input())
a1=int(input())
b1=int(input())
x2=int(input())
y2=int(input())
t1=x1*60+y1
t2=a1*60+b1
t0=2*t1-t2
t3=x2*60+y2
t_real=t3*2 - t0 + 1440
b2=t_real%60
a2=(t_real//60)%24
print(a2, b2)
