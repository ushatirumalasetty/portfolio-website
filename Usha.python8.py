usha=set((input()))
usha1=set((input()))
print(usha1.issubset(usha))




x=int(input())
a=1
for number in range(x):
    for number1 in range(0,x-number-1):
        print(" ",end="")
    for number1 in range(number+1,0,-1):
        print(number1,end="")
    for number1 in range (2,number+2):
        print(number1,end="")
    print("\n")



def char_frequency(str1):
    dict={}
    for n in str1:
        keys=dict.keys()
       # print(keys)
        if n in keys:
            dict[n]+=1
        else:
            dict[n]=1
    return dict
print(char_frequency('google.com'))


rows=int(input())
columns=int(input())
matrix=[]
for i in range (rows):
    matrix.append([])
for i in range (rows):
    for j in range (columns):
        matrix[i].append(j)
        matrix[i][j]=0
for i in range(rows):
    for j in range (columns):
        matrix[i][j]=int(input())
print(matrix)


SYMMETRIC DIFFERENCE OF SET


no1=input()
array1=input()
array1=set(array1.split(" "))
no2=input()
array2=input()
array2=set(array2.split(" "))
k=len(array1.symmetric_difference(array2))
print(k)



SET OPERATIONS


no1=int(input())
array=input()
array=set(array.split(" "))
no=int(input())
sum=int(0)
while no!=0:
   array1=set(array)
   operation=input()
   operation=operation.split(" ")
   if operation[0]=="intersection_update":
        array2=input()
        array2=set(array2.split(" "))
        array1.intersection_update(array2)
   elif operation[0]=="update":
        array2=input()
        array2=set(array2.split(" "))
        array1.update(array2)
   elif operation[0]=="symmetric_difference":
        array2=input()
        array2=set(array2.split(" "))
        array1.symmetric_difference(array2)
   else:
        array2=input()
        array2=set(array2.split(" "))
        array1.difference_update(array2)
   no=no-1
for i in array1:
    k=int(i)
    sum=sum+k
print(sum)


WRAPPING OF TEXT

import textwrap
string=input()
width=int(input())
textwrap.wrap(string,width)
print(textwrap.fill(string,width))


PRINTIND PATTERN

t=input()
t=t.split(" ")
m=int(t[0])
n=int(t[1])
a=n
for i in range(m//2):
    p=(a-3)//2
    print(p*"-"+((n-2*p)//3)*".|."+p*"-")
    a=a-6
print(((n-7)//2)*"-"+"WELCOME"+((n-7)//2)*"-")
a=a+6
for i in range(m//2):
    p=(a-3)//2
    print(p*"-"+((n-2*p)//3)*".|."+p*"-")
    a=a+6

STRING FORMATTING

def print_formatted(number):
    for i in range(1,number+1):
        a=oct(i)
        b=hex(i).upper()
        c=bin(i)
        l=len(bin(number))-2
        i=str()
        print(i.rjust(l),a[2:].rjust(l),b[2:].rjust(l),c[2:].rjust(l))


number=int(input())
print_formatted(number)


LIST COMPREHENNSINS

x=int(input())
y=int(input())
z=int(input())
n=int(input())
b,a=[],[]
for i in range(x):
    for j in range(y):
        for k in range(z):
            if i+j+k!=n:
                a.append(i)
                a.append(j)
                a.append(k)
                b.append(a)
                a=[]
print(b)


RUNNER SCORE(SECOND MAXIMUM)



m=int(input())
n=int(input())
a,b=[],[]
for i in range(m):
       a.append(input().split(","))
for i in range(m):
    for i in range(n):
        print(a[i][j])