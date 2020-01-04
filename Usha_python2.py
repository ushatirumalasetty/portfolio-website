operation=input()
usha=[]
usha1=[]
while True:
    if operation.find(" ")==4:
        usha.append(operation[5:])
    elif operation=="POP":
        if usha==[]:
            print("Empty Stack")
        else:
            usha.pop()
    elif operation=="PRINT":
        usha1=list(usha)
        usha1.reverse()
        for x in usha1:
            print(x)
    else:
        break
    operation=input()