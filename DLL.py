class Node:
    def __init__( self, data ):
        self.data=data
        self.next=None
        self.tail=None
class DoublyLinkedList:
    def __init__( self ):
        self.head=None
        self.tail=None #NUll
    
    def InsertAtEnd(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
        else:
            
            newnode.prev=self.tail
            self.tail.next=newnode
            self.tail=newnode

    def InsertAtBeginning(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
    def InsertAtPosition(self,data,position):
        newnode=Node(data)
        temp=self.head                 
        while(position-1!=0):#It is for position after "for position before put -2"
            temp=temp.next
            position-=1
        newnode.prev=temp
        newnode.next=temp.next
        temp.next=newnode
        newnode.next.prev=newnode
    
    def DeleteAtEnd(self):
        if self.head==None:
            print("List is Empty")
        elif self.head.next==None:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
    
    def DeleteAtFirst(self):
        if self.head==None:
            print("List is empty")
        elif self.head.next==None:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next  
            self.head.prev=None
    
    def DeleteAtPosition(self,position):
        if pos==1:
            self.head=self.head.next
            self.head.prev=None
        else:
            temp=self.head
            while(pos-2!=0):
                temp=temp.next
                position-=1
            temp.next=temp.next

    def Display(self):
        temp=self.head
        while(temp!=None):
            print(hash(temp),temp.data,hash(temp.next))
            temp=temp.next
dll=DoublyLinkedList() 
dll.InsertAtEnd(2)
dll.InsertAtEnd(3)
dll.InsertAtEnd(5)
dll.InsertAtEnd(6)
dll.Display()
print()
dll.InsertAtBeginning(1)
dll.Display()
print()
dll.InsertAtPosition(4,3)
dll.Display()
dll.DeleteAtEnd()
print()
dll.Display()
print()
dll.DeleteAtFirst()
dll.Display()
print()
dll.DeleteAtPosition(2)


