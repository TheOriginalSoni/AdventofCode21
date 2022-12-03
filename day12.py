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
    aa = line.replace("start","0").replace("end","1")
    a1 = aa.split("-")[0]
    a2 = aa.split("-")[1]
    a.append([a1,a2])
    a.append([a2,a1])

auni = list(set(sum(a,[])))

a2 = {}
for x in auni:
    a2[x]=[]

for b in a:
    a2[b[0]].append(b[1])

st = [['0']]
ans = 0
while(len(st)>0):
    curr = st.pop()
    currp = curr[len(curr)-1]
    if(currp == '1'):
       ans = ans + 1
       continue
    
    for nbr in a2[currp]:
        if(nbr.islower() and nbr in curr):
            continue
        if(nbr == '0'):
            continue
        if(nbr == currp):
            continue
        currt = curr.copy()
        currt.append(nbr)
        st.append(currt)
        
print(ans)

st = [['0']]
ans = 0
while(len(st)>0):
    curr = st.pop()
    currp = curr[len(curr)-1]
    if(currp == '1'):
       ans = ans + 1
       #print(curr)
       continue
    
    for nbr in a2[currp]:
        flag = 1
        if(nbr.islower() and curr.count(nbr)>1):
            flag = 0
        if(nbr == '0'):
            flag = 0
        if(nbr.islower() and curr.count(nbr)==1):
            curr2 = list(filter(lambda x: x.islower(),curr))
            for i in curr2:
                if(curr2.count(i)>1):
                    flag=0
        if(flag):
            currt = curr.copy()
            currt.append(nbr)
            st.append(currt)
        
print(ans)
