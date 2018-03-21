import sys
from functools import reduce
def bubble(l):
    l = list(l)
    i = 0
    count = 0
    while count < len(l):
        if l[i].isupper():
            l.append(l.pop(i))
        else:
            i += 1
        count += 1
    return reduce(lambda x,y: x+y,l)
if __name__ == '__main__':
    while True:
        s = sys.stdin.readline().strip()
        if not s:
            break
        result = bubble(s)
        print(result)
