x=input()
b=x[0]
k=len(x)
usha=""
for a in x:
    if a==b:
        continue
    else:
        usha=usha+b
        b=a
usha=usha+b
print(usha)