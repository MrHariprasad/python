class Node:
    def __init__( self, data ):
        self.data=data
        self.next=None
class SinglyLinkedList:
    def __init__( self ):
        self.head=None #NUll
    
    def InsertAtEnd(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=newnode
    def InsertAtBeginning(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def InsertAtPosition(self,data,position):
        newnode=Node(data)
        temp=self.head                 
        while(position-1!=0):#It is for position after "for position before put -2"
            temp=temp.next
            position-=1
        newnode.next=temp.next
        temp.next=newnode
    
    def DeleteAtEnd(self):
        if self.head==None:
            print("List is Empty")
        elif self.head.next==None:
            self.head=None
        else:
            temp=self.head
            while(temp.next.next!=None):
                temp=temp.next
            temp.next=None
    
    def DeleteAtFirst(self):
        if self.head==None:
            print("List is empty")
        else:
            temp=self.head
            self.head=temp.next  #self.head=self.head.next
    
    def DeleteAtPosition(self,position):
        if self.head==None:
            print('list is empty')
        else:
            while(position-1!=0):
                temp=temp.next
                position-=1
            temp.next=temp.next

    def Display(self):
        temp=self.head
        while(temp!=None):
            print(hash(temp),temp.data,hash(temp.next))
            temp=temp.next
sll=SinglyLinkedList() 
sll.InsertAtEnd(2)
sll.InsertAtEnd(3)
sll.InsertAtEnd(5)
sll.InsertAtEnd(6)
sll.Display()
print()
sll.InsertAtBeginning(1)
sll.Display()
print()
sll.InsertAtPosition(4,3)
sll.Display()
sll.DeleteAtEnd()
print()
sll.Display()
print()
sll.DeleteAtFirst()
sll.Display()
print()
sll.DeleteAtPosition(2)


