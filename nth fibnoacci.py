def fibnonth(n):
    if n<=0:
        print( "invalid input")
    elif n==1:
        return 0
    else:
        return fibnonth(n-1)+fibnonth(n-2)
print(fibnonth(10))