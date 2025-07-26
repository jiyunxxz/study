n = int(input())
a = list(map(int,input().split())) #값을 입력받을때 몇개인지 모르는 경우 그냥 하나의 문자로 받으면 편함.리스트로 작성할것이라면더더욱
max = max(a)
l=[]
sum=0
for i in range(n):
    new = a[i-1]/max*100
    l.append(new)
for i in range(n):
    sum += l[i-1]
print(sum/n)
