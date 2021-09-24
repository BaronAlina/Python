a=int(input())
k=a%10
if(k==1)and(a!=11):
    print(str(a)+' korova')
elif((k==2)or(k==3)or(k==4))and(a!=12)and(a!=13)and(a!=14):
    print(str(a)+' korovy')
else:
    print(str(a)+' korov')
