import math
import sys
from collections import Counter
import heapq


def MII():
    return map(int, sys.stdin.readline().split())


def II():
    return int(sys.stdin.readline())


def LII():
    return list(MII())


def I():
    return sys.stdin.readline().strip()

def f (a,b,c):
    dx,dy=x[a]-x[c],y[a ]-y[c]
    dx2,dy2=x[b]-x[c],y[b ]-y[c]
    return abs(dx*dy2-dx2*dy)
n=II()
x=[]
y=[]
for i in range(n):
    a,b=MII()
    x.append(a)
    y.append(b)
cur=-1
cnt=sys.maxsize
for i in range(1,n):
    if abs(x[i]-x [0])==cnt:
        if abs(y[i]-y[0])<abs(y[cur]-y[0]):
            cur=i
    if abs(x[i]-x [0])<cnt:
        cur=i
        cnt=abs(x[i]-x[0])
cnt=-1
q=-1
for i in range(1,n):
    if i==cur:
        continue
    if f(0,cur,i) and (cnt==-1 or f(0,cur,i)<cnt):
        cnt=f(0,cur,i)
        q=i
print(1,cur+1,q+1)
