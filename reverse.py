def reverse(n,r):
    if n<=0:
        return r
    else:
        rem=n%10
        r=(rem)+r*10
        return reverse(n//10,r)
        
r=0
print(reverse(123456789,r))