class graph:
    def __init__(self):
        self.d={}
    def insert(self,a,b):
        if a in self.d:
            self.d[a].append(b)
        else:
            self.d[a]=[]
            self.d[a].append(b)
g=graph()
g.insert(1,2)
g.insert(1,3)
g.insert(2,4)
g.insert(2,5)
g.insert(3,6)
g.insert(3,7)
print(g.d)
