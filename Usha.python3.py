x=int(input())
r=[]
while x!=0:
    r.append(x%10)
    x//=10
r.reverse()
print(len(r))
