lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

def conv(s):
    if(s[0]=='f'):
        return 1
    if(s[0]=='d'):
        return 3
    if(s[0]=='u'):
        return 4
    return 0

a = []
for line in lines:
    b = line.split()
    n=int(b[1])
    y = conv(b[0])
    a.append((y,n))
    
f=0
d=0
for b in a:
    if(b[0]==1):
        f=f+b[1]
    else:
        d=d+(b[1]*pow(-1,b[0]-3))

print(d*f)

aim=0
d=0
f=0
for b in a:
    if(b[0]>=3):
        aim=aim+(b[1]*pow(-1,b[0]-3))
    else:
        f=f+b[1]
        d=d+aim*b[1]

print(d*f)
