class node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
a=node(1)
b=node(2)
c=node(3)
a.left=b
a.right=c
print(a.data)
print(a.left.data)
print(a.right.data)
