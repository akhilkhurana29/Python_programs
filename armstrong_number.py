a = input()
i=0
sum=0
while i < len(a):
    sum += pow(int(a[i]),len(a))
    i+=1
if sum == int(a):
    print("armstrong!")
else:
    print("try another number")