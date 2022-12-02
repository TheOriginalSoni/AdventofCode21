import re
from collections import Counter

lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

a = [int(x) for x in lines[0].split(",")]

def tr(n):
    if(n<=1):
        return n
    return ((n+1)*n)//2

ans = [sum([abs(f-x) for x in a]) for f in range(max(a)+1)]
print(min(ans))

ans = [sum([tr(abs(f-x)) for x in a]) for f in range(max(a)+1)]
print(min(ans))
