n=20
global c
tab=[0]*(n+1)
tab[0]=0
tab[1]=1
c=0
for i in range(2,n+1): 
    c+=1
    tab[i]=tab[i-1]+tab[i-2]
print(tab[n])
print(c)
