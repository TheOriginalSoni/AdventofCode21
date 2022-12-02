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

a = [[int(x) for x in list(line)] for line in lines]
#print(a)

n=len(a)
m=len(a[0])

c =[]
c2=[]
for i in range(len(a)):
    for j in range(len(a[i])):
        x=0
        if(i<=0 or a[i][j]<a[i-1][j]):
            x = x+1
        if(i>=n-1 or a[i][j]<a[i+1][j]):
            x = x+1
        if(j<=0 or a[i][j]<a[i][j-1]):
            x = x+1
        if(j>=m-1 or a[i][j]<a[i][j+1]):
            x = x+1
        if(x==4):
            c.append(a[i][j])
            c2.append((i,j))

d = sum([x+1 for x in c])
print(d)

adj = []
for i in range(len(a)):
    for j in range(len(a[i])):
        if(i>0 and a[i][j]<=a[i-1][j]):
            adj.append([(i,j),(i-1,j)])
        if(i<n-1 and a[i][j]<=a[i+1][j]):
            adj.append([(i,j),(i+1,j)])
        if(j>0 and a[i][j]<=a[i][j-1]):
            adj.append([(i,j),(i,j-1)])
        if(j<m-1 and a[i][j]<=a[i][j+1]):
            adj.append([(i,j),(i,j+1)])

#print(adj)

ans = [[[]for y in range(m)] for x in range(n)]
#print(ans)

for b in c2:
    visited = set()
    st = [b]
    while(len(st)>0):
        curr = st.pop(0)
        #print(f"curr = {curr}")
        if (curr in visited):
            continue
        visited.add(curr)
        
        d= list(filter(lambda x: x[0]==curr,adj))
        #print(d)
        for y in d:
            st.append(y[1])
    
    #print(b)
    #print(visited)
    
    for curr in visited:
        ans[curr[0]][curr[1]].append(b)

#print(ans)

d = {}
for b in c2:
    d[b]=[]


disp = [["." for y in range(m)] for x in range(n)]

for i in range(len(a)):
    for j in range(len(a[i])):
        if(len(ans[i][j])==1 and a[i][j]!=9):
            b = ans[i][j][0]
            ix = c2.index(b)
            disp[i][j]=ix
            d[b].append((i,j))


for i in range(len(a)):
    for j in range(len(a[i])):
        print(disp[i][j],end="")
    print()


#print(d)
e = [len(d[x]) for x in d]
e.sort(reverse=True)

print(e[0]*e[1]*e[2])
