lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

a=[]
for line in lines:
    letter = [ord(x)-ord('0') for x in line]
    a.append(letter)

count = [0] * len(a[0])
for b in a:
    for c in range(len(b)):
        if(b[c]==1):
            count[c]=count[c]+1

least=0
most=0
for b in count:
    if(b>len(a)-b):
        most=most*2+1
        least=least*2+0
    else:
        most=most*2+0
        least=least*2+1

print(most*least)

amost = a.copy()
aleast= a.copy()

i=0
while(len(amost)>1):
    s0 = [b[i] for b in amost].count(0)
    s1 = [b[i] for b in amost].count(1)
    if(s0<=s1):
        s=1
    else:
        s=0
    
    amost=list(filter(lambda x: x[i]==s,amost))
    i=i+1

i=0
while(len(aleast)>1):
    s0 = [b[i] for b in aleast].count(0)
    s1 = [b[i] for b in aleast].count(1)
    if(s0<=s1):
        s=0
    else:
        s=1
    
    aleast=list(filter(lambda x: x[i]==s,aleast))
    i=i+1

am = int(''.join([str(i) for i in amost[0]]),2)
al = int(''.join([str(i) for i in aleast[0]]),2)

print(am*al)
