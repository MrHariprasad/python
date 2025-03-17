c=0
n=5
memo=[0]*(n+1)
def fun(x):
    if memo[x]:
        return memo[x]
    global c
    c+=1
    if x<=1:
        return x
    else:
        memo[x]=fun(x-1)+fun(x-2)
        return memo[x]
print(fun(n))
print(c)
print(memo)
