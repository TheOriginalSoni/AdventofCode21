import re
from collections import Counter
from itertools import permutations


'''
lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)
'''

with open('testcases.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n',"") for x in lines]

a=[]
for line in lines:
    b = [int(x) for x in list(line)]
    a.append(b)

#print(a)

d = [[-1 for x in a[0]] for y in a]

d[0][0]=0

st = []
st.append((0,0))

while(len(st)>0):
    m = min(d[i][j] for i,j in st)
    x = list(filter(lambda x:d[x[0]][x[1]]==m,st))[0]
    idx = st.index(x)

    curr = st.pop(idx)
    i,j = curr
    print(f"{i},{j},{len(st)} - ")
    i2,j2 = i+1,j
    if(i2>=0 and i2<len(d) and j2>=0 and j2<len(d[0])):
        if(d[i2][j2]==-1 or d[i2][j2]>d[i][j]+a[i2][j2]):
            d[i2][j2] = d[i][j]+a[i2][j2]
            if((i2,j2) not in st):
                st.append((i2,j2))
    i2,j2 = i-1,j
    if(i2>=0 and i2<len(d) and j2>=0 and j2<len(d[0])):
        if(d[i2][j2]==-1 or d[i2][j2]>d[i][j]+a[i2][j2]):
            d[i2][j2] = d[i][j]+a[i2][j2]
            if((i2,j2) not in st):
                st.append((i2,j2))
    i2,j2 = i,j+1
    if(i2>=0 and i2<len(d) and j2>=0 and j2<len(d[0])):
        if(d[i2][j2]==-1 or d[i2][j2]>d[i][j]+a[i2][j2]):
            d[i2][j2] = d[i][j]+a[i2][j2]
            if((i2,j2) not in st):
                st.append((i2,j2))
    i2,j2 = i,j-1
    if(i2>=0 and i2<len(d) and j2>=0 and j2<len(d[0])):
        if(d[i2][j2]==-1 or d[i2][j2]>d[i][j]+a[i2][j2]):
            d[i2][j2] = d[i][j]+a[i2][j2]
            if((i2,j2) not in st):
                st.append((i2,j2))

print(d[len(d)-1][len(d[0])-1])

a2 = a.copy()
for t in range(4):
    for i in range(len(a)):
        a2[i] = a2[i] + [x+t+1 for x in a[i]]

a3 = a2.copy()
for t in range(4):
    a3 = a3 + [[y+t+1 for y in x] for x in a2]

a3 = [[y%9 if y%9!=0 else 9 for y in x] for x in a3]

#print(len(a3))
#print(len(a3[0]))

'''
for i in a3:
    for j in i:
        print(j,end="")
    print()
'''

a = a3.copy()

d = [[-1 for x in a[0]] for y in a]

d[0][0]=0

st = []
st.append((0,0))

while(len(st)>0):
    m = min(d[i][j] for i,j in st)
    x = list(filter(lambda x:d[x[0]][x[1]]==m,st))[0]
    idx = st.index(x)

    curr = st.pop(idx)
    i,j = curr
    #print(f"{i},{j},{len(st)} -")
    i2,j2 = i+1,j
    if(i2>=0 and i2<len(d) and j2>=0 and j2<len(d[0])):
        if(d[i2][j2]==-1 or d[i2][j2]>d[i][j]+a[i2][j2]):
            d[i2][j2] = d[i][j]+a[i2][j2]
            if((i2,j2) not in st):
                st.append((i2,j2))
    i2,j2 = i-1,j
    if(i2>=0 and i2<len(d) and j2>=0 and j2<len(d[0])):
        if(d[i2][j2]==-1 or d[i2][j2]>d[i][j]+a[i2][j2]):
            d[i2][j2] = d[i][j]+a[i2][j2]
            if((i2,j2) not in st):
                st.append((i2,j2))
    i2,j2 = i,j+1
    if(i2>=0 and i2<len(d) and j2>=0 and j2<len(d[0])):
        if(d[i2][j2]==-1 or d[i2][j2]>d[i][j]+a[i2][j2]):
            d[i2][j2] = d[i][j]+a[i2][j2]
            if((i2,j2) not in st):
                st.append((i2,j2))
    i2,j2 = i,j-1
    if(i2>=0 and i2<len(d) and j2>=0 and j2<len(d[0])):
        if(d[i2][j2]==-1 or d[i2][j2]>d[i][j]+a[i2][j2]):
            d[i2][j2] = d[i][j]+a[i2][j2]
            if((i2,j2) not in st):
                st.append((i2,j2))

print(d[len(d)-1][len(d[0])-1])
