#with arguments with return type
def Addition(a,b):
    c=a+b
    return c

if __name__=="__main__":
    print("with arguments with return type")
    a=int(input())
    b=int(input())
    print(Addition(a,b))

#with arguments without return type

def Addition(a,b):
    c=a+b
    print(c)

if __name__=="__main__":
    print("with arguments without return type")
    a=int(input())
    b=int(input())
    Addition(a,b)
    
#without arguments with return type

def Addition():
    a=int(input())
    b=int(input())
    c=a+b
    return c

if __name__=="__main__":
    print("without arguments with return type")
    print(Addition())

#without arguments without return type

def Addition():
    a=int(input())
    b=int(input())
    c=a+b
    print(c)

if __name__=="__main__":
    print("without arguments without return type")
    Addition()
