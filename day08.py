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
#print(lines)

actual = [("ABCEFG",0),("CF",1),("ACDEG",2),("ACDFG",3),("BCDF",4),("ABDFG",5),("ABDEFG",6),("ACF",7),("ABCDEFG",8),("ABCDFG",9)]
act0 = [''.join(sorted(x[0])) for x in actual]
act0.sort()
act0 = " ".join(act0)
#print(act0)
actd = dict(actual)

a = []
for line in lines:
    bt = line.split("|")
    b0 = list(filter(None,bt[0].split(" ")))
    b1 = list(filter(None,bt[1].split(" ")))
    a.append((b0,b1))

c = sum([b[1] for b in a],[])
d = list(filter(lambda x: len(x) in [len(actual[i][0]) for i in [1,4,7,8]],c))

print(len(d))

l1 = 'abcdefg'
l2 = 'ABCDEFG'

ans = []
for b in a:
    for p in list(permutations(range(7))):
        b0 = b[0]
        b1 = b[1]
        #print(p)
        for i in range(len(p)):
            b0 = [x.replace(l1[i],l2[p[i]]) for x in b0]
        b0 = [''.join(sorted(x)) for x in b0]
        b0.sort()
        b0 = " ".join(b0)
        
        if(b0==act0):
            break

    for i in range(len(p)):
        b1 = [x.replace(l1[i],l2[p[i]]) for x in b1]
    
    b1 = [''.join(sorted(x)) for x in b1]
    c= int("".join([str(actd[x]) for x in b1]))
    
    ans.append(c)
    #print(b1)
    #print(c)
    #print(b0)

print(sum(ans))
