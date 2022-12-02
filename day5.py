import re
from collections import Counter

lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

a=[]
for line in lines:
    b=[int(x) for x in re.split(r'[> \-,]+', line)]
    a.append(b)

maxx = max(list(sum([(b[0],b[2]) for b in a],())))
maxy = max(list(sum([(b[1],b[3]) for b in a],())))

#print(a)
#print(maxx)

c=[]
for b in a:
    if(b[0]==b[2]):
        for i in range(min(b[1],b[3]),max(b[1],b[3])+1):
            c.append((b[0],i))
    elif(b[1]==b[3]):
        for i in range(min(b[0],b[2]),max(b[0],b[2])+1):
            c.append((i,b[1]))

d = Counter(c)
e = len(list(filter(lambda x: x>1,[d[b] for b in d])))

print(e)

c=[]
for b in a:
    if(b[0]==b[2]):
        for i in range(min(b[1],b[3]),max(b[1],b[3])+1):
            c.append((b[0],i))
    elif(b[1]==b[3]):
        for i in range(min(b[0],b[2]),max(b[0],b[2])+1):
            c.append((i,b[1]))
    elif(abs(b[1]-b[3])==abs(b[0]-b[2])):
        i=b[0]
        j=b[1]
        while(i!=b[2]):
            c.append((i,j))
            i = i+1 if i<b[2] else i-1
            j = j+1 if j<b[3] else j-1 
        c.append((b[2],b[3]))

d = Counter(c)
e = len(list(filter(lambda x: x>1,[d[b] for b in d])))

'''
for i in range(maxx+1):
    for j in range(maxy+1):
        print("." if d[(j,i)]==0 else d[(j,i)],end="")
    print()
'''
print(e)
