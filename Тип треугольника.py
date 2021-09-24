a=int(input())
b=int(input())
c=int(input())
if (c >= (a + b)) or (b >= (a + c)) or (a >= (b + c)):
  print('impossible')
else:
    if(c**2==(a**2+b**2))or(b**2==(a**2+c**2))or(a**2==(c**2+b**2)):
        print('rectangular')
    elif(c**2>(a**2+b**2))or(b**2>(a**2+c**2))or(a**2>(c**2+b**2)):
        print('obtuse')
    elif(c**2<(a**2+b**2))or(b**2<(a**2+c**2))or(a**2<(c**2+b**2)):
        print('acute')
    

