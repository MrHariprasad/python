#case-1:printing while going
'''
def fun(n):
    if n==11:
         return  
    print(n)
    fun(n+1)
fun(1)
'''
#case-2
'''
def fun(n):
    if n==11:
         return "biscuit"  
    print(n)
    print(fun(n+1)) #it is returning bisciut at value 10 after it reached 11 back to 10   
fun(1)
'''
#case-returning biscuit back
'''
def fun(n):
    if n==11:
         return  "biscuit"
    print(n)
    return fun(n+1)
print(fun(1))
'''
#case-going printing coming back by printing and returning biscuit
'''
def fun(n):
    if n==11:
         return "biscuit" 
    print(n)
    a=fun(n+1)
    print(n)
    return a
print(fun(1))
'''