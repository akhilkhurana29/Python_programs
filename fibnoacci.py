a=0
b=1
n=int(input())
print(a, end=" ")
for i in range(0,n):
    c=a+b
    print(c, end=" ")
    a=b
    b=c