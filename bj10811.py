a=[]
temp = 0
l=[]
n,m = map(int,input().split())
for i in range(1,n+1):
    a.append(i)
for i in range(m):
    i,j = map(int,input().split())
    for t in range(i,j+1):
        # temp = a[i-1]
        # a[i-1] = a[j-1]
        # a[j-1] = temp
        for k in range(i,j+1):
            l.append(a[k-1])
        l = l[::-1]
        for u in range(i,j+1):
            a.insert((u-1),l[k-1])
print(*a)