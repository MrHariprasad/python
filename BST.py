class node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class bst:
    def __init__(self):
        self.root=None
    def insert(self,data):
        newnode=node(data)
        if self.root==None:
            self.root=newnode
        else:
            curr=self.root
            while(curr):
                if data<curr.data:
                    if curr.left==None:
                        curr.left=newnode
                        break
                    else:
                        curr=curr.left
                else:
                    if curr.right==None:
                        curr.right=newnode
                        break
                    else:
                        curr=curr.right
                    


    def inorder(self):
        curr=self.root
        def helper(curr):
            if curr:
                helper(curr.left)
                print(curr.data)
                helper(curr.right)
        helper(curr)
r=bst()
r.insert(5)
r.insert(3)
r.insert(6)
r.inorder()
        
