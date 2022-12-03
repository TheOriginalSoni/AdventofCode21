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

'''PART 1'''
s = lines[0]

a=[]
for line in lines[2:]:
    b1=line[0:2]
    b2=line[-1].lower()
    a.append([b1,b2])

for t in range(10):
    for x in a:
        b1 = x[0]
        b2 = x[1]
        s=s.replace(b1,b1[0]+b2+b1[1])
        s=s.replace(b1,b1[0]+b2+b1[1])
    s=s.upper()

s2 = Counter(list(s))
s3 = [s2[i] for i in s2]

print(max(s3)-min(s3))

'''PART 2'''
s = lines[0]

d = {}
dempt = {}

for i in range(26):
    for j in range(26):
        cc = chr(ord('A')+i)+chr(ord('A')+j)
        d[cc]=0
        dempt[cc]=0

for i in range(len(s)-1):
    d[s[i:i+2]]=1

a=[]
for line in lines[2:]:
    b1=line[0:2]
    b2=line[-1] #.lower()
    a.append([b1,b2])

for t in range(40):
    d2=dempt.copy()

    for x in a:
        b1 = x[0]
        b2 = x[1]

        s1 = b1[0]+b2
        s2 = b2+b1[1]
        d2[s1]=d2[s1]+d[b1]
        d2[s2]=d2[s2]+d[b1]

    d=d2.copy()
    e = {x:y for x,y in d.items() if y!=0}

cnt = {}
for i in range(26):
    cnt[chr(ord('A')+i)]=0

for i in range(26):
    for j in range(26):
        c1 = chr(ord('A')+i)
        c2 = chr(ord('A')+j)
        cnt[c1] = cnt[c1] + d[c1+c2]
        cnt[c2] = cnt[c2] + d[c1+c2]        

cnt[s[0]] = cnt[s[0]]+1
cnt[s[len(s)-1]] = cnt[s[len(s)-1]]+1

e = [y for x,y in cnt.items() if y!=0]
print((max(e)-min(e))//2)
