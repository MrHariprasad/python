def fun(i,j,g):
    if i<0 or i>=len(g) or j <0 or j>=len(g[0]) or g[i][j]==0:
        return
    g[i][j]=0
    fun(i+1,j,g)
    fun(i-1,j,g)
    fun(i,j+1,g)
    fun(i,j-1,g)
    
g=[[1,1,1,1,1],[1,1,1,1,1,],[1,1,1,1,1],[1,1,1,1,1]]
c=0
for i in range(len(g)):
    for j in range(len(g[0])):
        if g[i][j]==1:
            c+=1
            fun(i,j,g)

print(c)













