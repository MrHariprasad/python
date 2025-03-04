#List
l=[1,2,3,4,5]

for i in range(0,len(l)):
    print(l[i],end=' ')

print()

for i in l:
    print(i,end=" ")
#List Input
'''
print()
l=list(map(int,input().split()))
print(l)
'''
#List inbuilt functions

l=[1,2,3,4]
print(len(l))
print(sum(l))
print(min(l))
print(max(l))

#To check built in functions of list
print(dir(list)) 

#append,clear,copy,count,extend,index,insert,pop,remove,reverse,sort

l=[1,2,3]
print(l)

l.append(4)
print(l)

l.extend([5,6,7])
print(l)

l.insert(4,8)
print(l)

l.pop()
print(l)

l.remove(2)
print(l)

l.clear()
print(l)
