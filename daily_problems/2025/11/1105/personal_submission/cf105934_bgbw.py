n=II()
s=LII()
ans =inf
cnt = 0
cur =s.copy()
for i in range(1, n ):
    if i%2:
        if cur [i ]>=cur[i-1 ]:
            cnt +=1+cur [i ]-cur[i-1 ]
            cur [i ]=cur [i -1 ]-1
    else:
        if cur [i]<=cur [i -1 ]:
            cnt +=1+cur [i-1 ]-cur [i ]
            cur [i ]=cur [i-1]+1
ans =cnt
cnt = 0
cur=s.copy()
for i in range(1, n ):
    if not i%2:
        if cur [i ]>=cur[i-1 ]:
            cnt +=1+cur [i ]-cur[i-1 ]
            cur [i ]=cur [i -1 ]-1
    else:
        if cur [i]<=cur [i -1 ]:
            cnt +=1+cur [i-1 ]-cur [i ]
            cur [i ]=cur [i-1]+1
ans=min(ans,cnt )
print(ans )
