lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

def disp(mat):
    for i in range(len(mat)):
        print(mat[i],end="")
        print()

a=[]
f= []
for line in lines:
    if(len(line)==0):
        continue
    if(line[0]=='f'):
        c = line[11:].split("=")
        f.append((c[0],int(c[1])))
    else:
        b = line.split(",")
        a.append([int(x) for x in b])

#print(a)
#print(f)

mx=max([x[0] for x in a])
my=max([x[1] for x in a])

a2 = [[0 for x in range(mx+1)] for y in range(my+1)]

for x in a:
    a2[x[1]][x[0]]= a2[x[1]][x[0]]+1

a3 = a2.copy()
#print(mx)
#print(my)

#disp(a2)
#print()

fmx = mx
fmy = my
for currf in f[0:1]:
    if(currf[0]=='x'):
        i=currf[1]
        while(i<=fmx):
            for j in range(0,fmy+1):
                i2 = currf[1]- (i-currf[1])
                j2 = j
                a2[j2][i2] = a2[j][i] + a2[j2][i2]
            i=i+1
        fmx = currf[1]
    else:
        j=currf[1]
        while(j<=fmy):
            for i in range(0,fmx+1):
                j2 = currf[1]- (j-currf[1])
                i2 = i
                a2[j2][i2] = a2[j][i] + a2[j2][i2]
            j=j+1
        fmy=currf[1]
    #disp(a2)      
    #print()

s=0
for i in range(fmx+1):
    for j in range(fmy+1):
        if(a2[j][i]>0):
            s=s+1
print(s)

fmx = mx
fmy = my
ti=1
for currf in f:
    #print(f"{ti} - {currf}")
    ti=ti+1
    if(currf[0]=='x'):
        i=currf[1]
        while(i<=fmx):
            for j in range(0,fmy+1):
                i2 = currf[1]- (i-currf[1])
                j2 = j
                a3[j2][i2] = a3[j][i] + a3[j2][i2]
            i=i+1
        fmx = currf[1]-1
    else:
        j=currf[1]
        while(j<=fmy):
            for i in range(0,fmx+1):
                j2 = currf[1]- (j-currf[1])
                i2 = i
                a3[j2][i2] = a3[j][i] + a3[j2][i2]
            j=j+1
        fmy=currf[1]-1
    #print(f"{fmx} {fmy}")
    #disp(a2)      
    #print()


for j in range(fmy+1):
    for i in range(fmx+1):
        if(a2[j][i]>0):
            print("#",end="")
        else:
            print(".",end="")
    print()

