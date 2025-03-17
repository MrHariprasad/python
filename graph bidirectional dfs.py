class graph:
    def __init__(self):
        self.d={}
    def insert(self,a,b):
        if a in self.d:
            self.d[a].append(b)
            if b in self.d:
                self.d[b].append(a)
            else:
                self.d[b]=[]
                self.d[b].append(a)
        else:
            self.d[a]=[]
            self.d[a].append(b)
            if b in self.d:
                self.d[b].append(a)
            else:
                self.d[b]=[]
                self.d[b].append(a)
    def dfs(self,root):
        q=[root]
        v=[root]
        while q:
            curr=q.pop()
            print(curr,end=" ")
            
            for i in self.d[curr]:
                if i not in v:
                    q.append(i)
                    v.append(i)
g=graph()
g.insert(1,2)
g.insert(1,3)
g.insert(2,4)
g.insert(2,5)
g.insert(3,6)
g.insert(3,7)
#print(g.d)
g.dfs(1)
