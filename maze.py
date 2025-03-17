def fun(i,j,g,v):
    if [i,j] in v:
        return 
    if i<0 or i>=len(g) or j <0 or j>=len(g[0]) or g[i][j]==0:
        return
    if g[i][j]=="g":
        return True
    print(i,j)
    v.append([i,j])
    return fun(i+1,j,g,v)or fun(i-1,j,g,v)or fun(i,j+1,g,v)or fun(i,j-1,g,v)

g=[["s",1,1,1,1],[0,0,0,1,0,],[1,0,0,1,1],[0,0,0,0,"g"]]
v=[]
for i in range(len(g)):
    for j in range(len(g[0])):
        if g[i][j]=="s":
            #print(fun(i,j,g,v))
            if fun(i,j,g,v):
                print("true")
            else:
                print("false")














