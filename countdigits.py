n=int(input())
if n<0:
    n=n*-1
count=0
while(n!=0):
    n=n//10
    count+=1
print(count)
#--------------
n=input()
if n[0]=='-1':
    print(len(n)-1)
else:
    print(len(n))
