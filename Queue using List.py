def Enqueue(data):
    global front 
    global rear 
    if front==-1 and rear==-1:
        queue.append(data)
        front=rear=0
        print(data,'is enqueued into queue')
    else:
        queue.append(data)
        rear+=1
        print(data,"is enqueued into queue")
def Dequeue():
    global front
    global rear
    if front==-1 and rear==-1:
        print("Queue is empty")
    elif front ==rear:
        print(queue[front],"id dequeud from queue")
        queue.pop(0)
        front=rear=-1
    else:
        print(queue[front],"is dequeued from queue")
        queue.pop(0)
        rear-=1
def Display():
    if queue:
        print(queue)
    else:
        print("Queue is empty")
if __name__=="__main__":
    queue=[]
    front=-1
    rear=-1
    print("\n***********Welcome to Queue Operations********")
    print("Enter 1 to Enqueue an element into Queue")
    print("Enter 2 to Dequeue an element into Queue")
    print("Enter 3 to Display all element into Queue")
    print('Enter -1 to EXIT\n')
    while(True):
        ip=int(input("Enter your choice"))
        if ip==1:
            data=int(input("Enter your Enqueue value: "))
            Enqueue(data)
        elif ip==2:
            Dequeue()
        elif ip==3:
            Display()
        elif ip==-1:
            print("you have Exited the program")
            break
        else:
            print("Invalid input")

