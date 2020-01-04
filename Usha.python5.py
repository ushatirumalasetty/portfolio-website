string1=input()
usha=string1.split(",")
k=len(usha)
usha1=[]
for a in usha:
    if usha.count(a)>k/2 and usha1.count(a)==0:
        print(a)
        usha1.append(a)
if len(usha1)==0:
    print("NONE")