a,b,c=map(int,input().split())
if(c<b):
        c,b=b,c
if (c<a):
        c,a=a,c
if(b<a):
        b,a=a,b
print(a,b,c)
if(a+b<=c):
        print("No")
elif(a*a+b*b<c*c ):
        print("Obtuse")
elif(a*a+b*b == c*c):
        print("Right")
elif(a*a+b*b>c*c):
        print("Acute")