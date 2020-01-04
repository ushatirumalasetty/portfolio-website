n=input()
a=input()
a= list(a.split(" "))
maximum=max(a)
for i in a:
    if i==maximum:
        a.remove(i)
print(a)
