lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

a=[]
for line in lines:
    b=[int(x) for x in list(line)]
    a.append(b)

def disp(atr):
    for x in atr:
        print("".join([str(y) for y in x]))

ans = 0
t=1
flag=0
while True:
    a2 = a.copy()
    a2 = [[x+1 for x in b] for b in a2]
    tmp = [[0 for x in b] for b in a2]
    
    st = []
    
    for i in range(len(a)):
        for j in range(len(b)):
            if(a2[i][j]>=10):
                st.append((i,j))
                tmp[i][j]=1
    
    while(len(st)>0):
        curr = st.pop()
        i=curr[0]
        j=curr[1]

        i2j2list = [(i+1,j),(i-1,j),(i,j+1),(i,j-1),(i-1,j-1),(i+1,j-1),(i-1,j+1),(i+1,j+1)]
        for curr in i2j2list:
            i2 = curr[0]
            j2 = curr[1]

            if(i2>=0 and i2<len(a2) and j2>=0 and j2 <len(a2[0])):
                a2[i2][j2]=a2[i2][j2]+1
                if(a2[i2][j2]>=10 and tmp[i2][j2]==0):
                    st.append((i2,j2))
                    tmp[i2][j2]=1

    f = len(list(filter(lambda x: x>=10,sum(a2,[]))))

    if(f==len(a2)*len(a2[0]) and flag==0):
        flag=t

    ans = ans+f
    
    a2 = [[0 if x>=10 else x for x in b] for b in a2]
    a=a2.copy()

    if(t==100):
        print(ans)

    t=t+1
    if(t>100 and flag):
        break

print(flag)
