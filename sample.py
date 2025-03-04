#OUTPUT
a=5;b=6
print(a,b)
print("a=%d b=%d"%(a,b),end=" ")
print("a={} b={}".format(a,b))
print("a={0} b={1}".format(a,b))
print("b={1} a={0}".format(a,b))

#INPUT
'''
a=input()
print(a)
a,b=input().split()
print(a,b)
'''

#Arithematic Operators

print("Arithematic Operators")
a=5;b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)#division
print(a//b)#floor division
print(a%b)#modulo division
print(a**b)

#Relational Operators

print("Relational Operators")
a=5;b=2
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

#Assignment Operators

print("Assignment Operators")
a=5;b=2
print(a)
a+=b #short hand operator
a=a+b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a//=b
print(a)
a=int(a)
a%=b
print(a)
a&=b
print(a)
a|=b
print(a)
a^=b
print(a)

#Logical Operators
print("Logical Operators")
#and
print(False and False)
print(False and True)
print(True and False)
print(True and True)
#or
print(False or False)
print(False or True)
print(True or False)
print(True or True)
#~
print(not True)
print(not False)

print(5>2 and print("abc"))
print(5<2 and print("abc"))

print(5>2 or print("abc"))
print(5<2 or print("abc"))

#Bitwise Operators

print("Bitwise Operators")
print(10 & 6)
print(10 | 6)
print(10 ^ 6)
print(10>>2)
print(10<<2)

#Identity Operators

print("Identity Operators")
a=5;b=5
print(a is b)
print(a is not b)

a=6;b=5
print(a is b)
print(a is not b)

#Membership Operator

print("Membership Operator")
print(1 in [5,1,4,8])
print(1 not in [5,1,4,8])

print(3 in (5,1,4,8))
print(3 not in (5,1,4,8))

