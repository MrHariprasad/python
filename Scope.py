def Function():
    print(a)#local scope

if __name__=="__main__":
    a=5
    Function()
    print(a)


def Function():
    print(a)#not local scope

if __name__=="__main__":
    Function()
    a=5

def Function():
    a=5

if __name__=="__main__":
    Function()
    print(a)