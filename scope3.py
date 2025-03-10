a=6#local variable
def Function():
    #print(a)#2
    a=5
    print(a)#3

if __name__=="__main__":
    print(a)#1
    Function()
    print(a)#4