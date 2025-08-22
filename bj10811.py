a=[]
n,m = map(int,input().split())
for i in range(1,n+1):
    a.append(i)
for u in range(m):
    i,j = map(int,input().split())
    a[i-1:j] = a[i-1:j][::-1] #슬라이싱에 대해서 자세히 파악하기. 시작점,끝점은미포함인데 시작점이 끝점보다 클 수 없다. 순서를 역순하고 싶을때는 2개의 대괄호를 써야함
    #반드시 다시 풀어볼것 
print(*a) 