lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

a=[]
for line in lines:
    b=list(line)
    a.append(b)

strt = ['[','{','(','<']
endb = [']','}',')','>']
pts = [57,1197,3,25137]

'''
): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points.
'''

'''
): 1 point.
]: 2 points.
}: 3 points.
>: 4 points.
'''
newpts = [2,3,1,4]

s=0
s2 = []
for b in a:
    st = []
    flag=0
    for c in b:
        if(c in strt):
            st.append(c)
        else:
            i = endb.index(c)
            pc = st.pop()
            if(strt[i]==pc):
                continue
            else:
                flag=pts[i]
                break
    s=s+flag
    if(flag==0 and len(st)>0):
        curr=0
        while(len(st)>0):
            c = st.pop()
            i = strt.index(c)
            curr = curr * 5 + newpts[i]
        s2.append(curr)

print(s)

s2.sort()
print(s2[(len(s2)-1)//2])
