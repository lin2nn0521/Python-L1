a,b=map(int,input().split())
if(a<b):
    a,b=b,a
r=a%b
while (r!=0):
    a=b
    b=r
    r=a%b
print(b)
