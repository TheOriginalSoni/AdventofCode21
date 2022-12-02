lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

bnumbers=[int(x) for x in lines[0].split(",")]
#print(bnumbers)

a=[]
b=[]
for i in range(2,len(lines)):
    line=lines[i]
    #print(line)
    idx=(i-1)%6
    if(idx==0):
        a.append(b)
        b=[]
    else:
        b.append([int(x) for x in lines[i].split()])
a.append(b)

def iswinner(b):
    for i in range(len(b)):
        if (sum(b[i])==-1*len(b)):
            return True
        c = [x[i] for x in b]
        if (sum(c)==-1*len(b)):
            return True
    return False

a1=a.copy()
i=0
win=[]
flag=True
while flag:
    num = bnumbers[i]
    a1=[[list(map(lambda x: -1 if x==num else x,c)) for c in b] for b in a1]
    for b in a1:
        if (iswinner(b)):
            win=b
            flag=False
    i=i+1
i=i-1

s= sum(list(filter(lambda x: x!=-1,sum(win, []))))
print(s*bnumbers[i])

a2=a.copy()
i=0
while(len(a2)>0):
    num = bnumbers[i]
    a2=[[list(map(lambda x: -1 if x==num else x,c)) for c in b] for b in a2]

    for b in a1:
        if (iswinner(b)):
            win=b
    a2 = list(filter(lambda b: iswinner(b)==False,a2))
    i=i+1
i=i-1

s= sum(list(filter(lambda x: x!=-1,sum(win, []))))
print(s*bnumbers[i])
